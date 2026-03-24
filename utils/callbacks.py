import os

def environment_callback(request):
    env = os.getenv("ENV", "dev")
    env_mapping = {
        "prod": ["Production", "danger"],
        "staging": ["Staging", "warning"],
        "dev": ["Development", "info"],
        "local": ["Local", "success"],
    }
    return env_mapping.get(env, ["Unknown", "info"])

def environment_title_prefix_callback(request):
    env = os.getenv("ENV", "dev")
    prefix_mapping = {"prod": "[PROD]", "staging": "[STAGING]", "dev": "[DEV]", "local": "[LOCAL]"}
    return prefix_mapping.get(env, "[UNKNOWN]")

def dashboard_callback(request, context):
    context.update({"sample": "example"})
    return context
