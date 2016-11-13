# -*- coding: utf-8 -*-


def get_db():
    return "USE talkingdata;"

def drop_table(table_name):
    return "DROP TABLE IF EXISTS `%s`;" % table_name

"""
fields = {
    "keys": [],
    "attributes": []
}
"""
def create_table(table_name, fields):
    content = []
    for i, column_name in enumerate(fields["keys"]):
        content.append("`" + column_name + "` " + fields["attributes"][i])
    content.append(
        "PRIMARY KEY (%s)" % fields["keys"][0]
    )
    sql = """
        CREATE TABLE IF NOT EXISTS `%s` (
            %s
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """ % (table_name, ",\n".join(content))
    return sql

def load_data(file_name, table_name, fields):
    columns_name = ", ".join(["`" + s + "`" for s in fields["keys"][1:]])
    sql = """
        LOAD DATA LOCAL INFILE '%s'
        INTO TABLE %s
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\\n'
        IGNORE 1 LINES
        (%s);
    """ % (file_name, table_name, columns_name)
    return sql

def create_table_sql(file, fields):
    file_name = file + ".csv"
    table_name = file
    sql = [
        get_db(),
        drop_table(table_name),
        create_table(table_name, fields),
        load_data(file_name, table_name, fields)
    ]
    return "\n".join(sql)

def output_sql(sql_file, sql):
    with open(sql_file, 'w') as f:
        f.write(sql)


def app_events(name):
    fields = {
        "keys": [
            "app_events_id",
            "app_id",
            "event_id",
            "is_installed",
            "is_active"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "INT NOT NULL",
            "BIGINT NOT NULL",
            "VARCHAR(10) NOT NULL",
            "VARCHAR(10) NOT NULL"
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)


def app_labels(name):
    fields = {
        "keys": [
            "app_labels_id",
            "app_id",
            "label_id"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "BIGINT NOT NULL",
            "INT NOT NULL"
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)


def events(name):
    fields = {
        "keys": [
            "events_id",
            "event_id",
            "device_id",
            "timestamp",
            "longitude",
            "latitude"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "INT NOT NULL",
            "BIGINT NOT NULL",
            "DATETIME NOT NULL",
            "VARCHAR(10) NOT NULL",
            "VARCHAR(10) NOT NULL"
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)


def gender_age_test(name):
    fields = {
        "keys": [
            "gender_age_test_id",
            "device_id"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "BIGINT NOT NULL",
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)


def gender_age_train(name):
    fields = {
        "keys": [
            "gender_age_train_id",
            "device_id",
            "gender",
            "age",
            "group"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "BIGINT NOT NULL",
            "CHAR(1) NOT NULL",
            "SMALLINT NOT NULL",
            "VARCHAR(10) NOT NULL"
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)



def label_categories(name):
    fields = {
        "keys": [
            "label_categories_id",
            "label_id",
            "category"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "BIGINT NOT NULL",
            "VARCHAR(20)"
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)



def phone_brand_device_model(name):
    fields = {
        "keys": [
            "phone_brand_device_model_id",
            "device_id",
            "phone_brand",
            "device_model"
        ],
        "attributes": [
            "INT NOT NULL AUTO_INCREMENT",
            "BIGINT NOT NULL",
            "VARCHAR(20)",
            "VARCHAR(20)"
        ]
    }
    sql = create_table_sql(name, fields)
    output_sql("%s.sql" % name, sql)


app_events("app_events")
app_labels("app_labels")
events("events")
gender_age_test("gender_age_test")
gender_age_train("gender_age_train")
label_categories("label_categories")
phone_brand_device_model("phone_brand_device_model")
