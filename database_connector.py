import pyodbc

class DatabaseConnector:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def connect(self):
        try:
            #Postgres on google cloud
            self.connection = pyodbc.connect("Driver={PostgreSQL Unicode};Server=" + self.server + ";Database=" + self.database + ";Uid=" + self.username + ";Pwd=" + self.password + ";")
            self.cursor = self.connection.cursor()
            print("Connected to database")
        except:
            print("Connection to database failed")
            raise

    def disconnect(self):
        self.connection.close()
        print("Disconnected from database")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except:
            print("Query execution failed")
            raise

    def execute_query_with_result(self, query):
        try:
            self.cursor.execute(query)
            print("Query executed successfully")
            return self.cursor.fetchall()
        except:
            print("Query execution failed")
            raise

    def create_table(self, table_name, columns):
        try:
            columnsStatement = ""
            for column in columns:
                if column == columns[-1]:
                    columns += " TEXT"
                else:
                    columns += " TEXT, "
            self.cursor.execute("CREATE OR REPLACE TABLE " + table_name + " (" + columnsStatement + ")")
            self.connection.commit()
            print("Table created successfully")
        except:
            print("Table creation failed")
            raise

    def drop_table(self, table_name):
        try:
            self.cursor.execute("DROP TABLE " + table_name)
            self.connection.commit()
            print("Table dropped successfully")
        except:
            print("Table drop failed")
            raise

    def create_recipe_table(self):
        try:
            self.create_table("Recipes", ["name", "url", "ingredients", "instructions"])
        except:
            print("Recipe table creation failed")
            raise

    def insert_recipe(self, recipe):
        try:
            self.cursor.execute("INSERT INTO Recipes (name, url, ingredients, instructions) VALUES (?, ?, ?, ?)", recipe.get_name(), recipe.get_url(), recipe.get_ingredients(), recipe.get_instructions())
            self.connection.commit()
            print("Recipe inserted successfully")
        except:
            print("Recipe insertion failed")
            raise

    def get_all_recipes(self):
        try:
            return self.execute_query_with_result("SELECT * FROM Recipes")
        except:
            print("Getting all recipes failed")
            raise
