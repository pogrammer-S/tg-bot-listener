CREATE TABLE IF NOT EXISTS messages(
    id serial PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    message_user VARCHAR(255) NOT NULL,
    date_message VARCHAR(255) NOT NULL
);