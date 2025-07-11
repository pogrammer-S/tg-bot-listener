CREATE TABLE IF NOT EXISTS messages(
    id serial PRIMARY KEY,
    user_id INT NOT NULL,
    message_user VARCHAR(255) NOT NULL,
    date_message INT NOT NULL
);

CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    t_id INT NOT NULL,
    t_name VARCHAR(255) NOT NULL,   
    created_date INT NOT NULL
);

CREATE TABLE IF NOT EXISTS attachments(
    id serial PRIMARY KEY,
    user_id INT NOT NULL,
    mime_type VARCHAR(255) NOT NULL,
    paths TEXT NOT NULL
);