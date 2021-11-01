# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:27:02 2021

@author: mahsh
"""
import sqlite3
from sqlite3 import Error
import pandas as pd

class Model():
    """School data management model"""
    def __init__(self):
        self.conn = sqlite3.connect('./data/school_management.db')
        
    def createRecordsFromCSV(self):
        """Create School DataBase from CSV files(students.csv, grades.csv, courses.csv)"""
        sql_create_students_table = '''CREATE TABLE IF NOT EXISTS students (
                    ID integer PRIMARY KEY AUTOINCREMENT, SEX text, LAST_NAME varchar(20) NOT NULL, 
                    FIRST_NAME varchar(20), EMAIL varchar(20), GROUP_NAME varchar(20)
                );'''
        sql_create_grades_table = '''CREATE TABLE IF NOT EXISTS grades (
                    ID integer PRIMARY KEY AUTOINCREMENT, YEAR text, STUDENT_ID int NOT NULL, 
                    COURSE varchar(20) NOT NULL, GRADE float
                );'''
        sql_create_courses_table ='''CREATE TABLE IF NOT EXISTS courses (ID integer PRIMARY KEY AUTOINCREMENT, COURSE text);'''

        if self.conn is not None:
            self.create_table(sql_create_students_table)
            self.create_table(sql_create_grades_table)
            self.create_table(sql_create_courses_table)
            
            # load the data into a Pandas DataFrame
            students = pd.read_csv('./data/students.csv')
            grades = pd.read_csv('./data/grades.csv')
            courses = pd.read_csv('./data/courses.csv')
    
            # write the data to a sqlite table
            students.to_sql('students', self.conn, if_exists='append', index = False)
            grades.to_sql('grades', self.conn, if_exists='append', index = False)
            courses.to_sql('courses', self.conn, if_exists='append', index = False)
        else:
            print("Error! cannot create the database connection.")
            


    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute(create_table_sql)
            cur.close()
        except Error as e:
            print(e)
            
    def getRecordsFromTable(self, table):
        """ load table from database to pandas dataframe 
        :params: database table (students, grades,...)
        :return: students dataframe
        """
        
        df = pd.read_sql_query(f"SELECT * FROM {table}", self.conn)
        df.reset_index(drop=True, inplace=True)
        return df
    
    def getAllRecords(self):
        """ load joined table of students and grades from database to pandas dataframe 
        :params:
        :return: students-grades dataframe
        """
        
        df = pd.read_sql_query("SELECT students.ID, students.SEX, students.LAST_NAME, \
                                students.FIRST_NAME, students.EMAIL, students.GROUP_NAME, \
                                grades.YEAR, grades.COURSE, grades.GRADE \
                                FROM grades \
                                LEFT JOIN students \
                                ON students.ID = grades.STUDENT_ID \
                                ORDER BY students.ID; ", self.conn)
        return df
            
    def addStudentRecord(self, id_, sex, lname, fname, email, group):
        """ add a new student to students table
        :params student record: id, sex, lastname, firstname, email, group
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM students WHERE EMAIL =?;', (email,))
    
            if cur.fetchone():
                print(f"Failed to add new student, student with Email:{email} already exist in the database.")
            else:   
                cur.execute("INSERT INTO students VALUES (NULL,?,?,?,?,?);",(sex, lname, fname, email, group))
                self.conn.commit()
            cur.close()
        except Error as e:
            print(e)
                
    def updateStudentRecord(self, id_, sex, lname, fname, email, group):
        """ modify student record in the students table
        :params student record: id, sex, lastname, firstname, email, group
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM students WHERE ID =?;', (id_,))
    
            if not cur.fetchone():
                print(f"Failed to update, no student record with ID:{id_} in the database.")
            else: 
                cur.execute('UPDATE students SET SEX=?, LAST_NAME=?, FIRST_NAME=?, EMAIL=?, GROUP_NAME=? WHERE ID=?', (sex, lname, fname, email, group, id_))
            
                self.conn.commit()
            cur.close()
        except Error as e:
            print(e)
            
    def addGradeRecord(self, year, stdID, course, grade):
        """ add a new grade to the grades table
        :params grade record: year, stdID, course, grade
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO grades VALUES (NULL,?,?,?,?);",(year, stdID, course, grade))
            self.conn.commit()
            cur.close()
        except Error as e:
            print(e)
            
    def updateGradeRecord(self, id_, year, stdID, course, grade):
        """ modify grade record in the grades table
        :params grade record: id, year, stdID, course, grade
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM grades WHERE ID =?;', (id_,))
    
            if not cur.fetchone():
                print(f"Failed to update, no grade record with ID:{id_} in the database.")
            else: 
                cur.execute('UPDATE grades SET YEAR=?, STUDENT_ID=?, COURSE=?, GRADE=? WHERE ID=?', (year, stdID, course, grade, id_))
            
                self.conn.commit()
            cur.close()
        except Error as e:
            print(e)
            
    
    def deleteRecord(self,table,id_):
        """ remove a record from table
        :param table: students or grades
        :param id_: id of the record
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM {table} WHERE id=?", (id_,))
            self.conn.commit()
            cur.close()
        except Error as e:
            print(e)
            
    def __del__(self):
        self.conn.close()
    
            
    
            
 
    