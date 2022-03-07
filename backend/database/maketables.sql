/*script for creating the schemas for necessary sql tables*/
CREATE TABLE restable (RestaurantID int, Time DateTime, PRIMARY KEY(RestaurantID));
CREATE TABLE reviewtable (RestaurantID int, UserID int, Rating int, Review VARCHAR(1000));
CREATE TABLE usertable (UserID int, UserName VARCHAR(30), Password VARCHAR(30),PRIMARY KEY(UserID));
CREATE TABLE userreviewstable (UserID int , RestaurantID int, Review VARCHAR(1000));
CREATE TABLE placestable (RestaurantID int,RestaurantName VARCHAR(20), Cuisine VARCHAR(20), Latitude float, Longitude float, PRIMARY KEY(RestaurantID));
ALTER TABLE restable ADD FOREIGN KEY (RestaurantID) REFERENCES placestable(RestaurantID);
ALTER TABLE reviewtable ADD FOREIGN KEY (RestaurantID) REFERENCES placestable(RESTAURANTID) ON DELETE CASCADE;
ALTER TABLE reviewtable ADD FOREIGN KEY (UserID) REFERENCES usertable(UserID) ON DELETE CASCADE;
ALTER TABLE userreviewstable ADD FOREIGN KEY (RestaurantID) REFERENCES placestable(RESTAURANTID) ON DELETE CASCADE;
ALTER TABLE userreviewstable ADD FOREIGN KEY (UserID) REFERENCES usertable(UserID) ON DELETE CASCADE;
