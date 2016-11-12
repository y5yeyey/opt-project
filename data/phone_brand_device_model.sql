USE talkingdata;
DROP TABLE IF EXISTS `phone_brand_device_model`;

        CREATE TABLE IF NOT EXISTS `phone_brand_device_model` (
            `phone_brand_device_model_id` INT NOT NULL AUTO_INCREMENT,
`device_id` BIGINT NOT NULL,
`phone_brand` VARCHAR(20),
`device_model` VARCHAR(20),
PRIMARY KEY (phone_brand_device_model_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'phone_brand_device_model.csv'
        INTO TABLE phone_brand_device_model
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`device_id`, `phone_brand`, `device_model`);
    