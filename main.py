from openAIAPI import AIModel


if __name__ == '__main__':
    testModel = AIModel()
    print(testModel.get_llm_response("allo"))