#  An iframe is used to embed HTML documents in other HTML documents
# We cannot click on elements present in iframe directly. To click on an element inside an iframe using XPath or any other locator,
# we need to switch to the frame first and then click.

# main steps:
"""
Step 1: Invoke browser and load web page
Step 2: Identify iframe using any locators
Step 3: Switch to iframe using switchTo method
Step 4: Act on elements inside iframe
Step 5: switch back to default content
"""

iframe_list =  driver.find_elements_by_tag_name("iframe")
length = len(iframe_list)
# print(length)

# we can switch to frames using 3 ways

# By using index of the frame
# By using Name or Id of the frame
# By using frame Web Element

