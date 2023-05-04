-- A SQL Script that creates a trigger that decreases the 
-- quantity of an item after adding a new order.:
CREATE TRIGGER decrease_quantity BEFORE INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_name = NEW.item_name;
