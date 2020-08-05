def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id).click()
        except NoSuchElementException:
        return False
        return True
        # print(check_exists_by_xpath(home))
def find_by_name():
    if (check_exists_by_id(id)) is True:
        driver.find_element_by_id(id).click()
        # print(‘xpath - pass’)
    else:
        driver.find_element_by_class_name(name).click()
        # print(‘xpath - fail > class - pass’)
        
    find_by_name()
