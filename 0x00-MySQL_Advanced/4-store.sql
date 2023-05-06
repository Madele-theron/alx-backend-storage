-- A SQL Script that creates a trigger that decreases the 
-- quantity of an item after adding a new order.:
CREATE TRIGGER DelQuantityConsult AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE NEW.item_name = name;
