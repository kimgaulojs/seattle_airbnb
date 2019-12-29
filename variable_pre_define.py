drop_col = [
    'scrape_id', # All same value
    'last_scraped', # All same value
    'experiences_offered', # all same value
    'city', # all same value
  'market', # all same value
  'country_code', # all same vaule
  'country', # all same value
  'smart_location', # all same value
  'zipcode', # usless
  'state', # all same value
  'street', # usless
  'has_availability', #all same value
  'calendar_last_scraped', #all same value
  'jurisdiction_names', #all same value
  'host_neighbourhood', #usless
  'neighbourhood', #usless
  'neighbourhood_group_cleansed',#usless
  'host_verifications', #useless
  'requires_license', #all same value
  'first_review', #52
  'last_review' #53
]

review_eval_col = [
    'review_scores_rating',
    'review_scores_accuracy',
    'review_scores_cleanliness',
    'review_scores_checkin',
    'review_scores_communication',
    'review_scores_location',
    'review_scores_value',
    'reviews_per_month'
]


cat_col_name = [
    'host_response_time', #1
    'property_type', #2
    'room_type', #3
    'bed_type', #4
    'cancellation_policy' #5
]

bool_col_name =[
    'host_is_superhost', #6
    'host_has_profile_pic', #7
    'host_identity_verified', #8
    'is_location_exact', #9
    'instant_bookable', #10
    'require_guest_profile_picture', #11
    'require_guest_phone_verification' #12
]

num_col_name = [
    'host_acceptance_rate', #13
    'host_response_rate', #14
    'calendar_updated', #15
    'beds', #16
    'bathrooms', #17
    'bedrooms', #18
    'review_scores_rating', #19
    'review_scores_accuracy', #20
    'review_scores_cleanliness', #21
    'review_scores_checkin', #22
    'review_scores_communication', #23
    'review_scores_location', #24
    'review_scores_value', #25
    'reviews_per_month', #26
    'number_of_reviews', #27
    'host_listings_count', #28
    'host_total_listings_count', #29
    'calculated_host_listings_count', #30
    'latitude', #31
    'longitude', #32
    'accommodates', #33
    'guests_included', #34
    'minimum_nights', #35
    'maximum_nights', #36
    'availability_30', #37
    'availability_60', #38
    'availability_90', #39
    'availability_365' #40
]

str_col_name = [
    'name', #41
    'summary', #42
    'space', #43
    'description', #44
    'neighborhood_overview', #45
    'transit', #46
    'host_name', #47
    'host_location', #48
    'host_about', #49
    'neighbourhood_cleansed' #50
]

date_col_name = [
    'host_since' #51
]

dic_bool = {
    't':1,
    'f':0
}

dic_cat = {
    'within an hour' : 4,
    'within a few hours' :3,
    'within a day':2,
    'a few days or more':1,
    
    'strict' : 'cacel_strict',
    'moderate' : 'cacel_moderate',
    'flexible' : 'cacel_flexible',
    
    'Entire home/apt':'Entire_H',
    'Private room':'Private_R',
    'Shared room':'Shared_R',
    
    
    'House':'House',
    'Apartment':'Apartment',
    
    'Townhouse':'Others',
    'Condominium':'Others',
    'Loft':'Others',
    'Bed & Breakfast':'Others',
    'Other':'Others',
    'Cabin':'Others',
    'Bungalow':'Others',
    'Camper/RV':'Others',
    'Boat':'Others',
    'Chalet':'Others',
    'Yurt':'Others',
    'Dorm':'Others',
    'Tent':'Others',
    'Treehouse':'Others',
    
    'Real Bed':'Real_B',
    'Futon':'Others_B',
    'Pull-out Sofa':'Others_B',
    'Airbed':'Others_B',
    'Couch':'Others_B'
}


dict_amenities_catagorize = {
    'Wireless Internet':'Internet', #1
    'Internet':'Internet', #2
    'Laptop Friendly Workspace':'Internet', #3
    
    'Heating':'Weather Control', #4
    'Air Conditioning':'Weather Control', #5
    'Indoor Fireplace':'Weather Control', #6
    
    'Hair Dryer':'Essentials', #7
    'Essentials':'Essentials', #8
    'Shampoo':'Essentials', #9
    'Hangers':'Essentials', #10
    'Iron':'Essentials', #11
    
    'Dryer':'Laundry Facility', #12
    'Washer':'Laundry Facility', #13
    'Washer / Dryer':'Laundry Facility', #14

    'Cable TV':'TV', #15
    'TV':'TV', #16

    'Elevator in Building':'Access Friendly', #17
    'Wheelchair Accessible':'Access Friendly', #18

    'Buzzer/Wireless Intercom':'Safety Feature', #19
    'Smoke Detector' :'Safety Feature', #20
    'Carbon Monoxide Detector':'Safety Feature', #21
    'Fire Extinguisher':'Safety Feature', #22
    'Safety Card':'Safety Feature', #23
    'Lock on Bedroom Door':'Safety Feature', #24
    'First Aid Kit':'Safety Feature', #25
    'Doorman':'Safety Feature', #26
    
    'Pets live on this property':'Pet Friendly', #27
    'Pets Allowed':'Pet Friendly', #28
    'Dog(s)':'Pet Friendly', #29
    'Cat(s)':'Pet Friendly', #30
    'Other pet(s)':'Pet Friendly', #31
    
#    
#     'Breakfast':'Breakfast', #32
#     '24-Hour Check-in':'24-Hour Check-in', #33
#     'Free Parking on Premises':'Free Parking on Premises', #34
#     'Hot Tub':'Hot Tub', #35
#     'Suitable for Events':'Suitable for Events', #36
#     'Smoking Allowed':'Smoking Allowed', #37
#     'Pool':'Pool', #38
#     'Gym':'Gym', #39
#     'Kitchen':'Kitchen', #40
#     'Family/Kid Friendly':'Family/Kid Friendly', #41
    
}

