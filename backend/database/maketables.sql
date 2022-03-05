CREATE TABLE restable (RestaurantID int, Time DateTime);
CREATE TABLE reviewtable (RestaurantID int, UserID int, Rating int, Review String);
CREATE TABLE usertable (UserID int, UserName String, Password String);
CREATE TABLE userreviewstable (UserID int , RestaurantID int, Review String);
CREATE TABLE placestable (RestaurantID int,RestaurantName String, Cuisine String, Latitude float, Longitude float);
