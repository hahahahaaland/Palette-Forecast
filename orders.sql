INSERT INTO orders
(artwork_id, customer_name, size, frame_type, canvas_finish, customization, commission_order, gift_wrap, final_price, order_date)
VALUES
(1, 'Rahul Sharma', 'Large', 'Wooden', 'Matte', 'Landscape theme', 'Yes', 'Yes', 12000, '2026-07-19'),

(2, 'Priya Nair', 'Medium', 'Metal', 'Glossy', 'None', 'No', 'No', 8500, '2026-07-19'),

(3, 'Arjun Patel', 'Small', 'Black', 'Matte', 'Custom colors', 'Yes', 'No', 9500, '2026-07-20'),

(1, 'Sneha Gupta', 'Large', 'Golden', 'Glossy', 'Gift message', 'No', 'Yes', 13500, '2026-07-20'),

(2, 'Vikram Singh', 'Medium', 'Wooden', 'Canvas', 'None', 'No', 'No', 8900, '2026-07-21');

SELECT * FROM orders;