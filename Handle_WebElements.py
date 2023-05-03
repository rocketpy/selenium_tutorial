# Examples

# Alert Pop-Ups
alert_popup = driver.switch_to.alert

# The accept() method - accepts the alert message
alert_popup = Alert(driver)
alert_popup.accept()

# The dismiss() method cancels the alert prompt
alert_popup = Alert(driver)
alert_popup.dismiss()

# The text() method retrieves and displays the text that is in the alert pop-up
alert_popup = Alert(driver)
# print(alert_popup.text)
