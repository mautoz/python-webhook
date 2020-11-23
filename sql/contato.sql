CREATE TABLE IF NOT EXISTS contato (
    id          SERIAL NOT NULL PRIMARY KEY,
    registro    TIMESTAMP not NULL,
    nome        text not NULL,
    email       text not NULL,
    conteudo    text not NULL    
);