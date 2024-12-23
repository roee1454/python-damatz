initial_prompt = """
הדרישה שתתבקש לעמוד בה יכולה להיות כל נושא הקשור בייצור או אספקה של מוצר או שירות. עליך לשאול לפחות שתי שאלות (ורצוי יותר) שיעזרו לך להבין טוב יותר את הדרישה ולהפיק מסמך מסודר שמפרט את הצרכים והתנאים הרלוונטיים.
על השאלות להיות ממוקדות וברורות, תוך התייחסות לפרטים החשובים לספק את הדרישה באופן מלא.
בנוסף, השאלות צריכות להיות ממוספרות בסעיפים
תתן לי את כל השאלות באותה התשובה ותשתדל לחסוך בטוקנים

דוגמאות לשאלות:
מהם המאפיינים הספציפיים של המוצר או השירות הדרוש (כמו גודל, צבע, תכונות טכניות וכו')?
מהו לוח הזמנים הנדרש לאספקה, והאם יש תאריכים חשובים שיש לעמוד בהם?
האם יש דרישות מיוחדות לאריזה, הובלה או תנאים אחרים שצריך לקחת בחשבון?
האם יש מגבלות תקציביות או דרישות כלשהן הנוגעות לעלויות הייצור או האספקה?
דרישה: {message}
"""