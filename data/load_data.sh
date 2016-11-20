#!/bin/bash

python sql.py

mysql -u"root" < db.sql
mysql -u"root" "talkingdata" < app_events.sql
mysql -u"root" "talkingdata" < app_labels.sql
mysql -u"root" "talkingdata" < events.sql
mysql -u"root" "talkingdata" < gender_age_test.sql
mysql -u"root" "talkingdata" < gender_age_train.sql
mysql -u"root" "talkingdata" < label_categories.sql
mysql -u"root" "talkingdata" < phone_brand_device_model.sql
