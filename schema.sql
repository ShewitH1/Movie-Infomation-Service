-- CREATE TABLE image (
--     image_id        SERIAL,
--     caption         VARCHAR(255)    NOT NULL,
--     image_link      VARCHAR(255)    NOT NULL,
--     author_user     VARCHAR(255)    NOT NULL,
--     created_at      TIMESTAMP       NOT NULL,
--     PRIMARY KEY (image_id)

-- );


-- INSERT INTO image (caption, image_link, author_user, created_at)
-- VALUES
--     ('Sunset at the beach', 'https://example.com/sunset.jpg', 'user123', TIMESTAMP '2024-04-09 18:30:00'),
--     ('Mountain landscape', 'https://example.com/mountain.jpg', 'user456', TIMESTAMP '2024-04-09 12:45:00'),
--     ('City skyline at night', 'https://example.com/city.jpg', 'user789', TIMESTAMP '2024-04-08 21:15:00'),
--     ('Field of flowers', 'https://example.com/flowers.jpg', 'user321', TIMESTAMP '2024-04-08 10:00:00'),
--     ('Urban street art', 'https://example.com/streetart.jpg', 'user654', TIMESTAMP '2024-04-07 15:20:00'),
--     ('Beachside resort', 'https://example.com/resort.jpg', 'user987', TIMESTAMP '2024-04-07 09:45:00'),
--     ('Snowy mountain peak', 'https://example.com/snowy_peak.jpg', 'user234', TIMESTAMP '2024-04-06 11:30:00'),
--     ('Rural countryside', 'https://example.com/countryside.jpg', 'user567', TIMESTAMP '2024-04-05 14:20:00'),
--     ('Ancient ruins', 'https://example.com/ruins.jpg', 'user890', TIMESTAMP '2024-04-04 16:50:00');

-- SELECT * FROM image;