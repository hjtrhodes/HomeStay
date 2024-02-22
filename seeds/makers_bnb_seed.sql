

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
    space_image_url VARCHAR(255),
    price_per_night DECIMAL(10, 2),
    available_from DATE,
    available_to DATE,
    user_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id) 
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    booking_start_date DATE,
    booking_end_date DATE,
    trip_length INT,
    booking_status VARCHAR(255),
    user_id INT,
    space_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(space_id) REFERENCES spaces(id)
);


INSERT INTO users (user_name, user_email, user_password) VALUES ('Bob Johnson', 'bjohnson@email.com', 'mysecretpassword');
INSERT INTO users (user_name, user_email, user_password) VALUES ('John Doe', 'johndoe@email.com', 'password123');
INSERT INTO users (user_name, user_email, user_password) VALUES   ('Alice Smith', 'alicesmith@email.com', 'securepwd');

INSERT INTO spaces (space_name, space_description, space_image_url, price_per_night, user_id) VALUES ('Cozy Cottage', 'A charming cottage in the countryside. Beautiful views that are perfect for a relaxing snooze.', 'https://res.cloudinary.com/dut4qf1bt/image/upload/v1708512829/HomeStay/Country_Cottage_rhjlza.jpg', 99.99, 1);
INSERT INTO spaces (space_name, space_description, space_image_url, price_per_night, user_id) VALUES ('City Apartment', 'Modern apartment in the heart of the city. Enjoy the hustle and bustle in the heart of New York!', 'https://res.cloudinary.com/dut4qf1bt/image/upload/v1708512829/HomeStay/City_Apartment_yeb5mx.webp', 150, 2);
INSERT INTO spaces (space_name, space_description, space_image_url, price_per_night, user_id) VALUES ('Beach House', 'Beachfront property with stunning views. Do not forget to pack your surfboard, because you will be needing it.', 'https://res.cloudinary.com/dut4qf1bt/image/upload/v1708537463/HomeStay/fp-home1_hsvx5m.jpg', 200, 3);

INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (CURRENT_DATE + INTERVAL '7 days', CURRENT_DATE + INTERVAL '14 days', EXTRACT(DAY FROM CURRENT_DATE + INTERVAL '14 days' - (CURRENT_DATE + INTERVAL '7 days')), 'Denied', 2, 2);
INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (CURRENT_DATE + INTERVAL '12 days', CURRENT_DATE + INTERVAL '21 days', EXTRACT(DAY FROM CURRENT_DATE + INTERVAL '21 days' - (CURRENT_DATE + INTERVAL '12 days')), 'Pending', 3, 3);
INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (CURRENT_DATE + INTERVAL '17 days', CURRENT_DATE + INTERVAL '28 days', EXTRACT(DAY FROM CURRENT_DATE + INTERVAL '28 days' - (CURRENT_DATE + INTERVAL '17 days')), 'Pending', 2, 3);
INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (CURRENT_DATE + INTERVAL '7 days', CURRENT_DATE + INTERVAL '35 days', EXTRACT(DAY FROM CURRENT_DATE + INTERVAL '35 days' - (CURRENT_DATE + INTERVAL '7 days')), 'Pending', 3, 2);
INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (CURRENT_DATE + INTERVAL '35 days', CURRENT_DATE + INTERVAL '42 days', EXTRACT(DAY FROM CURRENT_DATE + INTERVAL '42 days' - (CURRENT_DATE + INTERVAL '35 days')), 'Pending', 1, 2);
INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (CURRENT_DATE + INTERVAL '28 days', CURRENT_DATE + INTERVAL '49 days', EXTRACT(DAY FROM CURRENT_DATE + INTERVAL '49 days' - (CURRENT_DATE + INTERVAL '28 days')), 'Pending', 2, 1);
