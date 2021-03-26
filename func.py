def main(context):
    print(f"Method: {context['request'].method}")
    return "", 204
