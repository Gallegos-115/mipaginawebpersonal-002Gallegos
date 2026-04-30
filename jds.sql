CREATE POLICY "Users see own orders"
ON orders
FOR SELECT
USING (auth.uid() = user_id);