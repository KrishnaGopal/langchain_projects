from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()


def main():
    # Automatically looks for the GOOGLE_API_KEY environment variable
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    response = llm.invoke("tell somthing about your self?")
    print(response.text)
    print("Hello from langchain-course!")



if __name__ == "__main__":
    main()