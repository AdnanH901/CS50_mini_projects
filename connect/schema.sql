CREATE TABLE users (
    id           INTEGER,
    first_name   TEXT,
    last_name    TEXT,
    username     TEXT,
    "password"   TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE companies (
    id           INTEGER,
    industry     TEXT,
    "name"       TEXT,
    "location"   TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE academics (
    id           INTEGER,
    "name"       TEXT,
    "type"       TEXT,
    "location"   TEXT,
    founded      DATETIME,
    PRIMARY KEY(id)
);

CREATE TABLE userPeople (
    user_id_1    INTEGER,
    user_id_2    INTEGER,
    FOREIGN KEY(user_id_1) REFERENCES users(id),
    FOREIGN KEY(user_id_2) REFERENCES users(id)
);

CREATE TABLE userCompanies (
    user_id      INTEGER,
    company_id   INTEGER,
    "start_date" DATETIME,
    end_date     DATETIME,
    title        TEXT,
    FOREIGN KEY(user_id)    REFERENCES users(id),
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

CREATE TABLE userAcademics (
    school_id    INTEGER,
    user_id      INTEGER,
    "start_date" DATETIME,
    end_date     DATETIME,
    degree_date  TEXT,
    FOREIGN KEY(user_id)   REFERENCES users(id),
    FOREIGN KEY(school_id) REFERENCES academics(id)
);
