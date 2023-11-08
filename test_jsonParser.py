from playwright.sync_api import Page, expect
from utilities.resources import *


def test_jsonParsing(page: Page):
    page.goto(Resources.url)  # go to respective URL
    page.screenshot(path="1_URL.png")
    page.get_by_text("Table Data").click()  # click on Table Data
    page.screenshot(path="2_Click_Table_data.png")
    page.locator("#jsondata").clear()
    page.locator("#jsondata").fill(data.dump)  # input given data
    page.screenshot(path="3_Input_data.png")
    page.get_by_role("button", name="Refresh Table").click()  # click refresh table button
    page.screenshot(path="4_Result.png")  # saving final result PNG

    ## Asserting each and every cell with the given data ##

    expect(page.locator("xpath=//*[@id='dynamictable']/tr[2]/td[1]")).to_have_text(data.table101)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[2]/td[2]")).to_have_text(data.table102)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[2]/td[3]")).to_have_text(data.table103)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[3]/td[1]")).to_have_text(data.table201)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[3]/td[2]")).to_have_text(data.table202)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[3]/td[3]")).to_have_text(data.table203)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[4]/td[1]")).to_have_text(data.table301)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[4]/td[2]")).to_have_text(data.table302)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[4]/td[3]")).to_have_text(data.table303)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[5]/td[1]")).to_have_text(data.table401)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[5]/td[2]")).to_have_text(data.table402)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[5]/td[3]")).to_have_text(data.table403)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[6]/td[1]")).to_have_text(data.table501)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[6]/td[2]")).to_have_text(data.table502)
    expect(page.locator("xpath=//*[@id='dynamictable']/tr[6]/td[3]")).to_have_text(data.table503)
