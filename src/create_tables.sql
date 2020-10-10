CREATE TABLE responders (
	id serial PRIMARY KEY,
	firstname VARCHAR ( 250 ),
	lastname VARCHAR ( 250 ),
	email VARCHAR ( 255 ) NOT NULL,
	created_on TIMESTAMP
);

CREATE TABLE experiments (
	id serial PRIMARY KEY,
	name VARCHAR ( 50 ) NOT NULL,
	created_on TIMESTAMP
);

CREATE TABLE tests (
	id serial PRIMARY KEY,
	test_text VARCHAR ( 8192 ) NOT NULL,
	author VARCHAR ( 50 ) NOT NULL,
	experiment_id INT NOT NULL,
	group_id INT NOT NULL,
	created_on TIMESTAMP,
	category VARCHAR ( 50 ),
	FOREIGN KEY (experiment_id) REFERENCES experiments (id)
);

CREATE TABLE responses (
	id serial PRIMARY KEY,
	responder_id INT NOT NULL,
	test_id INT NOT NULL,
	score INT NOT NULL,
	created_on TIMESTAMP,
	FOREIGN KEY (responder_id) REFERENCES responders (id),
	FOREIGN KEY (test_id) REFERENCES tests (id)
);
