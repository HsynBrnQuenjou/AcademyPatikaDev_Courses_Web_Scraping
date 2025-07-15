from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://academy.patika.dev/paths")
time.sleep(5)

# Yalnızca <section id="courses"> altındaki ders kartlarını al
course_section = driver.find_element(By.ID, "courses")
courses = course_section.find_elements(By.CSS_SELECTOR, 'a[data-testid="course-card"]')

data = []

for course in courses:
    try:
        course_type = course.find_element(By.TAG_NAME, "span").text.strip()
        if course_type.lower() != "ders":
            continue

        title = course.find_element(By.CLASS_NAME, "chakra-text").text.strip()
        href = course.get_attribute("href")
        rating = course.find_element(By.CLASS_NAME, "css-xofb8z").text.strip()
        meta = course.find_elements(By.CLASS_NAME, "css-y4v1s2")

        user_count = meta[0].text if len(meta) > 0 else ""
        point_value = meta[1].text if len(meta) > 1 else ""
        duration = meta[2].text if len(meta) > 2 else ""

        data.append({
            "Kurs Adı": title,
            "Puan": rating,
            "Kullanıcı Sayısı": user_count,
            "Puan Değeri": point_value,
            "Süre": duration,
            "Bağlantı": href,
            "Tip": course_type
        })

    except Exception as e:
        print("⚠️ Hata:", e)
        continue

driver.quit()

# Excel'e kaydetmeden önce tekrarları temizle
df = pd.DataFrame(data)
df.drop_duplicates(subset=["Kurs Adı"], inplace=True)
df.to_excel("academypatikadev_courses.xlsx", index=False)

print("✅ Yalnızca path-altı dersler kaydedildi.")
