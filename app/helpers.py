# app/helpers.py

def explain_jenkins_error(log: str) -> str:
    if "No such DSL method" in log:
        return (
            "This error usually means you're using a pipeline step or DSL "
            "function in Jenkins that is not recognized. This can happen if:\n"
            "- The plugin providing the DSL method isn't installed.\n"
            "- You have a typo in the method name.\n"
            "- The script is using declarative vs scripted pipeline wrongly.\n"
            "✅ Fix: Double-check your Jenkinsfile and make sure required plugins are installed."
        )
    elif "hudson.AbortException" in log:
        return (
            "A build was aborted due to an error or timeout. "
            "Check the logs before this line for more info on the failure cause."
        )
    else:
        return "Sorry, I couldn't understand this Jenkins error yet. Try providing more context or share the full error message."
