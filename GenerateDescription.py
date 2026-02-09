#!/usr/bin/python3

fruits_data = {
    "red_apple.txt": "Red Apple\n0.45 lbs\nRed Apple contains significant levels of dietary fiber and antioxidants. Consuming apples can assist in regulating blood sugar and improving heart health. Due to its high concentration of flavonoids, regular consumption plays an important role in boosting immune function and supporting digestive health.",
    "banana.txt": "Banana\n0.26 lbs\nBanana contains higher levels of potassium and vitamin B6 than most common fruits. Eating bananas can help regulate blood pressure and provide a sustained energy boost. Due to its essential mineral content, regular consumption plays an important role in supporting muscle function.",
    "green_grapes.txt": "Green Grapes\n1.15 lbs\nGreen Grapes contain high levels of polyphenols and vitamin K. Consuming grapes can help protect against oxidative stress and support bone health. Due to their high water and antioxidant content, regular consumption plays an important role in keeping the body hydrated.",
    "orange.txt": "Orange\n0.40 lbs\nOrange contains exceptionally high levels of vitamin C and folate. Eating oranges can significantly boost the immune system and enhance iron absorption. Due to its rich citric acid and vitamin content, regular consumption plays an important role in skin repair.",
    "watermelon.txt": "Watermelon\n20.0 lbs\nWatermelon contains higher levels of lycopene and citrulline. Consuming watermelon can improve circulation and reduce muscle soreness. Due to its high water content and array of vitamins, regular consumption plays an important role in maintaining optimal hydration."
}

def generate_txt_files():
    print("Generating txt files...")
    for fruit, description in fruits_data.items():
        with open(fruit, "w") as file:
            file.write(description)
    print("Txt files generated successfully.")

if __name__ == "__main__":
    generate_txt_files()
    