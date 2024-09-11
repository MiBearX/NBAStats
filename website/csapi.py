from flask import jsonify
from flask_restful import Resource
import sqlite3
from website.cs2 import csgoStashItems
import os


def validateWeaponType(wType):
    lowerWType = wType.lower()
    for formattedWeaponType in csgoStashItems.keys():
        if lowerWType == formattedWeaponType.lower():
            return formattedWeaponType


def validateWeaponName(wName, wType):
    lowerWName = wName.lower()
    for formattedWName in csgoStashItems[wType]:
        if lowerWName == formattedWName.lower():
            return formattedWName.replace("+", " ")

def processSQLRow(sqlRow, retData):
    (id, weaponName, skinName, rarity, weaponType, collection, imgURL, price, stPrice) = sqlRow
    retData.append({
        "weapon" : weaponName,
        "skinName" : skinName,
        "rarity" : rarity,
        "category" : weaponType,
        "collection" : collection,
        "imgURL" : imgURL,
        "price" : price,
        "StatTrackPrice" : stPrice
        })
    #printItem(weaponName, skinName, rarity, weaponType, collection, imgURL, price, stPrice)


class Weapon(Resource):

    def get(self, weaponType = None, weaponName = None):
        # Get the absolute path of the current directory
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Join it with your database filename
        DB_PATH = os.path.join(BASE_DIR, 'cs2Skins.db')
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        retData = []
        if weaponType is None:
            # queries all weapons
            query = "SELECT * FROM skins"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                processSQLRow(row, retData)
        elif weaponName is None:
            # queries all skins for specific weapon type
            weaponType = validateWeaponType(weaponType)
            query = "SELECT * FROM skins WHERE gun_type = ?"
            cursor.execute(query, (weaponType,))
            rows = cursor.fetchall()
            for row in rows:
                processSQLRow(row, retData)
        else:
            # queries skins for specific gun
            weaponName = validateWeaponName(weaponName, validateWeaponType(weaponType))
            query = "SELECT * FROM skins WHERE gun_name = ?"
            cursor.execute(query, (weaponName,))
            rows = cursor.fetchall()
            for row in rows:
                processSQLRow(row, retData)
        

        
        connection.commit()
        connection.close()
        return jsonify(retData)

