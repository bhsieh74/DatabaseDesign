# AirBnB MongoDB Analysis

## Data Set Details

The data set that I chose to complete this assignment on was the data set for AirBnB listings for the city of Cambridge, Massachusetts in the United States. The reason I chose this data set was because I used to live in Cambridge when I was younger, until I moved to New Jersey. So it was nostalgic to choose this city that I used to live in and seeing through some of the data, such as the neighborhoods and streets, it was a trip down memory lane. The dataset was retrieved from [this site](http://insideairbnb.com/get-the-data.html).  
The original data file was called listings.csv.gz. I used the gunzip command on the CIMS command line to unzip the file into a .csv file.   
The below table is a snippet of the raw data (.csv) file. Because the columns are too long to fit reasonably into markdown, I only displayed the first 20 rows but with only the first 5 column fields. 
| id | listing_url | scrape_id | last_scraped | name |
|---|---|---|---|---|
|  8521 |  https://www.airbnb.com/rooms/8521 | 20210225210417  | 2021-02-27  | SunsplashedSerenity walk to Harvard & Fresh Pond  |
|  11169 |  https://www.airbnb.com/rooms/11169 | 20210225210417  | 2021-02-26  | Lovely Studio Room: Thu-Mons  |
| 11945  |  https://www.airbnb.com/rooms/11945 | 20210225210417  |  2021-02-26 | Near Harvard: Safe & Lovely Room  |
| 19581  |  https://www.airbnb.com/rooms/19581 |  20210225210417 | 2021-02-26  | Furnished suite, Windsor  |
| 22006  |  https://www.airbnb.com/rooms/22006 |  20210225210417 | 2021-02-26  | B & B near Harvard's Quad Houses  |
|  24063 |  https://www.airbnb.com/rooms/24063 | 20210225210417  | 2021-02-26  | Riverbend Bed and Breakfast  |
| 26531  | https://www.airbnb.com/rooms/26531  |  20210225210417 | 2021-02-26  |  CENTRAL LOCATION IN HEART OF CAMBRIDGE |
|27498   |  https://www.airbnb.com/rooms/27498 |  20210225210417| 2021-02-26  |  Furnished suite 2 @ the Windsor |
| 79762  |  https://www.airbnb.com/rooms/79762 |  20210225210417 |  2021-02-25 | Cambridge Getaway @ Harvard & MIT |
|106474   | https://www.airbnb.com/rooms/106474  |  20210225210417 | 2021-02-26  |  large furnished suite in Central s |
| 108898  | https://www.airbnb.com/rooms/108898  |  20210225210417 | 2021-02-26  | The Treehouse  |
| 219471  | https://www.airbnb.com/rooms/219471  |  20210225210417 | 2021-02-25  |  A+ Clean & Safe 1Br @ MIT |
|  326170 | https://www.airbnb.com/rooms/326170  |  20210225210417 | 2021-02-26  |  Two-room suite near Harvard Univ. with parking |
| 405144  |https://www.airbnb.com/rooms/405144  | 20210225210417  | 2021-02-25  |  Apartment in Harvard's Backyard |
| 445407  | https://www.airbnb.com/rooms/445407  | 20210225210417  | 2021-02-26  |  East Cambridge Apartment |
| 456429  | https://www.airbnb.com/rooms/456429  | 20210225210417  | 2021-02-26  |  Elegant Airy Comfort. Workspace |
| 577384  | https://www.airbnb.com/rooms/577384  | 20210225210417  | 2021-02-27  |  Large Room with Shared Bath |
| 675441  | https://www.airbnb.com/rooms/675441  | 20210225210417  | 2021-02-27  |  Waterfront-1 Bed Room Luxury Condo |
| 715532  | https://www.airbnb.com/rooms/715532  | 20210225210417  | 2021-02-26  |  Quiet, Artistically Decorated Cambridge Apartment |
| 742574  | https://www.airbnb.com/rooms/742574  | 20210225210417  | 2021-02-26  |  See Yourself in Central Square |

There were not many problems with the original data set. As a result, I did not use Python or other software to scrub the data. The only problem, though miniscule, with the data set was that some records contained missing values, however there were few. 

## MongoDB Data Analysis
Because each document is extremely long, like the raw data file, I only displayed the first 3 documents but with only the first 5 column fields for each query. 

1. Show exactly two documents from the listings collection in any order  
```
db.listings.find().limit(2)
```
This query simply shows two listings from the collection.  

| id | listing_url | scrape_id | last_scraped | name |
|---|---|---|---|---|
| 19581  |  https://www.airbnb.com/rooms/19581 |  20210225210417 | 2021-02-26  | Furnished suite, Windsor  |
|  8521 |  https://www.airbnb.com/rooms/8521 | 20210225210417  | 2021-02-27  | SunsplashedSerenity walk to Harvard & Fresh Pond  |

2. Show exactly 10 documents in any order, but print in easier to read format and noting the host names for further use, using the pretty() function
```
db.listings.find().limit(10).pretty()
```

Similar to the first query, this query shows 10 documents from the collection, but it is outputted from the MongoDB client in a pretty, easy to read format. 
| id | listing_url | scrape_id | last_scraped | name |
|---|---|---|---|---|
| 19581  |  https://www.airbnb.com/rooms/19581 |  20210225210417 | 2021-02-26  | Furnished suite, Windsor  |
|  8521 |  https://www.airbnb.com/rooms/8521 | 20210225210417  | 2021-02-27  | SunsplashedSerenity walk to Harvard & Fresh Pond  |
|  11169 |  https://www.airbnb.com/rooms/11169 | 20210225210417  | 2021-02-26  | Lovely Studio Room: Thu-Mons  |

3. Choose two host_names who are superhosts (available in the host_is_superhost field), and show all of the listings offered by either of the two hosts
```
db.listings.find({
    $or:
        [{host_name: "Kevin",},
        {host_name: "Paul",},],
    }, 
    {   
        _id: 0,
        name: 1,
        beds: 1, 
        neighbourhood: 1, 
        review_scores_rating: 1, 
        price: 1,}
);
```
This query shows all of the listings by Kevin or Paul, two superhosts. I know Kevin and Paul are superhosts because in the cleaned dataset, both of these hosts have the field of "t" for their superhost field. I used the or operator to perform this query to get all listings from either Kevin OR Paul and used a projection that only showed the name, beds, neighbourhood, review_scores_rating, and price. 
| name | neighbourhood | beds | price | review_scores_rating |
|---|---|---|---|---|
| Cambridge Getaway @ Harvard & MIT  |  Cambridge, Massachusetts, United States |  3 | $250.00  | 97  |
|  Victorian Charm MIT/Harvard/Kendall/Central-1BR |   Cambridge, Massachusetts, United States | 2  | $113.00  |97  |
|  Cambridge Getaway @ MIT and Harvard |   Cambridge, Massachusetts, United States | 4  | $250.00  | 98  |

4. Find all the unique host_name values
```
db.listings.distinct("host_name")
```
This query simply returned a long list of host names. I believe the distinct function returned the host names in alphabetical order. 
| host_name |
| ----------|
|\We Are Kai & Nina|
|Aaron|
|Abe|

5. Find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as neighbourhood_group_cleansed in the data file), ordered by review_scores_rating descending
```
db.listings.find({
    beds: 
        {
            $gte: 2,
        }, 
    neighbourhood_cleansed: "The Fort",
    }, 
    {
        _id: 0, 
        name: 1, 
        beds: 1, 
        neighbourhood: 1, 
        review_scores_rating: 1, 
        price: 1,
    }
)
.sort({
    review_scores_rating: -1
})
```
This query returned all listings that have more than 2 beds in "The Fort" neighbourhood. I used the find function to match all listings that had greater than or equal to 2 beds and then matched the neighbourhood_cleansed to "The Fort". Then, I used a projection that only showed the name, beds, neighbourhood, review_scores_rating, and price. Lastly, I used the sort function to sort by the review ratings in descending order. 
| name | neighbourhood | beds | price | review_scores_rating |
|---|---|---|---|---|
| Perfect Location, Top Floor Apt |  Cambridge, Massachusetts, United States |  2 | $76.00  | 100  |
|  SoloPrivate Space |   Cambridge, Massachusetts, United States | 2  | $80.00  | 100  |
|  Cambridge Apt, walk to MIT, Harvard |   Cambridge, Massachusetts, United States | 4  | $120.00  | 98  |

6. Show the number of listings per host
```
let grouper = {
    $group: {
        _id: "host_name",
        listingCount: {$sum: 1}
    }
}
db.listings.aggregate([grouper])
```
I used the aggregate function to group the collection by host names, then used the sum function to sum up all of the number of listings per host. 
| _id | listingCount |
|-----|--------------|
| Brian + Heather | 2|
| Sofia | 1 |
| Anvita | 2 |

7. In a particular neighborhood_group_cleansed of your choosing again, find the average review_scores_rating per neighborhood, and only show the ones above a 95, sorted in descending order of rating
```
let group = {
    $group: {
        _id: "$neighbourhood_cleansed",
        avgRating: {$avg: "$review_scores_rating"},
    }
};

let match = {
    $match: {
        avgRating: {$gte: 95},
    }
};

let sort = {
    $sort: {
        avgRating: -1
    }
}
db.listings.aggregate([group, match, sort])
```
Similar to the previous query, I used the aggregate function once again to calculate the average score per neighbourhood, filtered only by neighbourhoods with an average score above 95. I first defined my group variable to group all of the "neighbourhood_cleansed" fields and then used the average function to average the "review_scores_rating" field. Then, I defined the match variable to only match the new documents that have above a 95 average rating. Lastly, I defined the sort variable to sort by average rating in descending order. Putting all of those variables together, I used the aggregate function and used all of them as parameters. 
| _id | avgRating |
|-----|--------------|
| Cambridgeport | 96.07594936708861|
| Riverside | 95.68571428571428 |
| East Cambridge| 95.2467532467324 |