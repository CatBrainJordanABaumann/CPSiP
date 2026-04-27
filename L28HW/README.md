- Tool Name and Purpose
    Crop Purchase Analyzer: This tool serves to calculate important
primarily financial information about a given crop and its seeds. This tool, in addition to calculating raw financials, also considers space usage and time to grow all of the seeds purchased. This tool could be quite useful as to allow for easier comparison between multiple crops. Such a purpose is quite important as when a farm is deciding which crop/s to plant, small changes can be incredibly drastic and slip ups of a few cents can snowball into thousands of wasted dollars or easily more depending on how important a place the mistake was in. For instance, the knowledge that growing potatoes a given year might result in quicker harvests but lower profits may incentivize a farmer to use potatoes if they expect to soon start being busier and if they would benefit from having more time off but would not feel the burden of decreased profits substantially.

- Installation
    The only dependency is standard so install like normal.

- Usage Example:
from tool import analyze_crop_purchase
analyze_crop_purchase(0.25, 15.17, 1, 3, 4)
Should result in the value { purchase_quantity = 60, purchase_quantity_unit = "seeds", expected_profit = 45.0, expected_profit_unit = "$", total_harvests = 15, total_harvests_unit = "crops", wait_time = 45, wait_time_unit = "days"}

- How This Fits the SNAP Project
    This will not fit into the SNAP project most likely. Our team has still not met to discuss what we are to do so I did this completely individually off of one of the example scenarios.