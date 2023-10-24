

DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    user_email VARCHAR(255),
    user_password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    space_name VARCHAR(255),
    space_description TEXT,
    price_per_night DECIMAL(10, 2),
    available_from DATE,
    available_to DATE,
    user_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id) 
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    booking_date DATE,
    booking_status VARCHAR(255),
    user_id INT,
    space_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(space_id) REFERENCES spaces(id)
);


INSERT INTO users (user_name, user_email, user_password) VALUES ('Bob Johnson', 'bjohnson@email.com', 'mysecretpassword');
INSERT INTO users (user_name, user_email, user_password) VALUES ('John Doe', 'johndoe@email.com', 'password123');
INSERT INTO users (user_name, user_email, user_password) VALUES   ('Alice Smith', 'alicesmith@email.com', 'securepwd');

INSERT INTO spaces (space_name, space_description, price_per_night, available_from, available_to, user_id) VALUES ('Cozy Cottage', 'A charming cottage in the countryside.', 99.99, '2023-10-15', '2023-11-15', 1);
INSERT INTO spaces (space_name, space_description, price_per_night, available_from, available_to, user_id) VALUES ('City Apartment', 'Modern apartment in the heart of the city.', 150, '2023-10-10', '2023-11-10', 2);
INSERT INTO spaces (space_name, space_description, price_per_night, available_from, available_to, user_id) VALUES ('Beach House', 'Beachfront property with stunning views.', 200, '2023-10-20', '2023-11-20', 3);

INSERT INTO bookings (booking_date, booking_status, user_id, space_id) VALUES ('2023-10-18','Confirmed', 1, 1);
INSERT INTO bookings (booking_date, booking_status, user_id, space_id) VALUES ('2023-10-12', 'Denied', 2, 2);
INSERT INTO bookings (booking_date, booking_status, user_id, space_id) VALUES ('2023-10-25', 'Pending', 3, 3);
INSERT INTO bookings (booking_date, booking_status, user_id, space_id) VALUES ('2023-10-25', 'Pending', 2, 3);
INSERT INTO bookings (booking_date, booking_status, user_id, space_id) VALUES ('2023-10-25', 'Pending', 3, 2);