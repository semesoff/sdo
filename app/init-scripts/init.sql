CREATE TABLE IF NOT EXISTS users
(
    id             INTEGER PRIMARY KEY,
    username       VARCHAR(64) UNIQUE NOT NULL,
    password       VARCHAR(255)       NOT NULL,
    roleType       VARCHAR(255)       NOT NULL DEFAULT 'student',
    studyGroup     VARCHAR(32),
    form_education VARCHAR(255),
    faculty        VARCHAR(255)
);

INSERT INTO users (id, username, password, roleType, studyGroup, form_education, faculty) VALUES
(1, 'teacher', '12345', 'teacher', 'null', 'null', 'Машиностроение'),
(2, 'student', '12345', 'student', '231-335', 'Бюджет', 'Информационные системы и технологии');