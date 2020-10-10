import psycopg2


def connect_to_pg():
    con = psycopg2.connect(database="deepmind", user="aioptify", password="deepminds7612", host="127.0.0.1", port="5432")
    print("Connected to db successfully!")
    cursor = con.cursor()
    return con, cursor


def load_tests(fn):
    tests = []
    with open(fn) as fp:
        for line in fp:
            test = line.strip()
            tests.append(test)
    return tests


def create_experiment(con, cursor, experiment_name):
    sql_string = "INSERT INTO experiments (name, created_on) VALUES ({}, NOW()) RETURNING id;".format(experiment_name)
    cursor.execute(sql_string);
    experiment_id = cursor.fetchone()[0]
    con.commit()
    print("A new experiment was created successfully!")
    return experiment_id


def add_test(con, cursor, data):
    test_text, author = data["text"], data["author"]
    category, experiment_id = data["category"], data["experiment_id"]
    group_id = data["group_id"]
    sql_string = "INSERT INTO tests (test_text, author, experiment_id, created_on, category, group_id) VALUES ('{}', '{}', {}, NOW(), '{}', {}) RETURNING id;".format(test_text, author, experiment_id, category, group_id)
    print(sql_string)
    cursor.execute(sql_string)
    con.commit()
    print("A new test was added successfully!")


def cleanup(con):
    con.close()


def run():
    con, cursor = connect_to_pg()
    # create a new experiment
    # experiment_name = "generic-books-tests-oct-2020"
    # experiment_id = create_experiment(con, cursor, experiment_name)
    # load human/gpt-2/gpt-3 tests
    fn = "experiment_1_oct_10_2020.csv"
    experiment_id = 1
    tests = load_tests(fn)
    for test in tests:
        res = test.split("`")
        group_id, author, category, test_text = int(res[0]), res[1], res[2], res[3]
        print("group_id: {}, category: {}, author: {}".format(group_id, category, author))
        data = {"text": test_text, "author": author, "category": category, "experiment_id": experiment_id, "group_id": group_id}
        # add_test(con, cursor, data)
    # close db connection
    cleanup(con) 

run()