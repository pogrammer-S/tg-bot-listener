CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL PRIMARY KEY,
    t_name VARCHAR(255) NOT NULL,
    created_date INT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages(
    user_id INT NOT NULL,
    message_text VARCHAR(255) NOT NULL,
    date_message INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS attachments(
    user_id INT NOT NULL,
    mime_type VARCHAR(255) NOT NULL,
    paths TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);