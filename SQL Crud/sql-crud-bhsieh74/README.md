# SQL CRUD

## SQL Code to create each of the required tables

#### Restaurants Table
```
create table restaurants (
    id INTEGER PRIMARY KEY,
    category TEXT,
    price TEXT,
    neighborhood TEXT,
    open INTEGER,
    close INTEGER,
    rating REAL,
    kids INTEGER
);
```

#### Review Table
```
create table reviews (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    comment TEXT
);
```

#### Users Table
```
create table users (
    id INTEGER PRIMARY KEY,
    email TEXT,
    password TEXT,
    handle TEXT
);
```

#### Posts Table
```
create table posts (
    id INTEGER PRIMARY KEY,
    message TEXT,
    date TEXT,
    story INTEGER,
    sender INTEGER,
    receiver INTEGER,
    seen INTEGER
);
```

## Link to each of the practice CSV data files in the data directory

[restaurants.csv](./data/restaurants.csv)
[reviews.csv](./data/reviews.csv)
[users.csv](./data/users.csv)
[posts.csv](./data/posts.csv)

## SQLite code to import the practice CSV data files into the tables

```
.mode csv
.headers on
.import restaurants.csv restaurants --skip 1;
.import reviews.csv reviews --skip 1;
.import users.csv users --skip 1;
.import posts.csv posts --skip 1;
```

## SQL queries that solve each of the tasks you were asked to do

### Part 1

#### 1. Find all cheap restaurants in a particular neighborhood (pick any neighborhood as an example).
```
SELECT * FROM restaurants WHERE neighborhood = "East Vilage";
```
#### 2. Find all restaurants in a particular genre (pick any genre as an example) with 3 stars or more, ordered by the number of stars in descending order.
```
SELECT * FROM restaurants WHERE category = "Pizzeria" AND rating > 3 ORDER BY rating DESC;
```
#### 3. Find all restaurants that are open now 
```
SELECT strftime('%H', 'now');
```
returns 20
```
SELECT * FROM restaurants WHERE open < 20 AND close > 20;
```
#### 4. Leave a review for a restaurant.
```
INSERT INTO reviews VALUES (3, "Good food!");
```
#### 5. Delete all restaurants that are not good for kids
```
DELETE FROM restaurants WHERE kids = 1;
```
#### 6. Find the number of restaurants in each NYC neighborhood
```
SELECT neighborhood, COUNT(neighborhood) FROM restaurants GROUP BY neighborhood;
```

### Part 2

#### 1. Register a new User.
```
INSERT INTO users values (1001, "newuser@gmail.com", "password", "new_user");
```
#### 2. Create a new Message sent by a particular User to a particular User (pick any two Users for example).
```
INSERT INTO posts values (2001, "This is a new message", "3/9/2021 3:54", 0, 613, 123, 0);
```
#### 3. Create a new Story by a particular User (pick any User for example).
```
INSERT INTO posts values (2002, "This is a new story", "3/9/2021 3:55", 1, 361, 163, 0);
```
#### 4. Show the 10 most recent visible Messages and Stories, in order of recency.
```
SELECT * FROM posts ORDER BY date DESC LIMIT 10;
```
#### 5. Show the 10 most recent visible Messages sent by a particular User to a particular User (pick any two Users for example), in order of recency.
```
SELECT * FROM posts WHERE sender = 298 AND receiver = 365 AND story = 0 AND seen = 0 ORDER BY date DESC LIMIT 10;
```
#### 6. Make all Stories that are more than 24 hours old invisible.
```
UPDATE posts SET seen = 1 WHERE (SELECT ROUIND((JULIANDAY('now') - JULIANDAY(posts.date)) * 60)) < 24;
```
#### 7. Show all invisible Messages and Stories, in order of recency.
```
SELECT * FROM posts WHERE seen = 1 ORDER BY date DESC;
```
#### 8. Show the number of posts by each User.
```
SELECT handle, COUNT(*) FROM users INNER JOIN posts ON users.id = posts.sender GROUP BY users.id;
```
#### 9. Show the post text and email address of all posts and the User who made them within the last 24 hours.
```
SELECT posts.message, users.email FROM posts, users WHERE posts.seen = 0 AND posts.story = 1;
```
#### 10. Show the email addresses of all Users who have not posted anything yet.
```
SELECT users.email FROM users WHERE NOT EXISTS (SELECT 1 FROM posts WHERE users.id = posts.sender);
```