from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

# Simulação da função J.A.R.V.I.S. (você substituirá por um modelo local depois)
def ask_jarvis(user_command: str) -> str:
    return f"Você disse: {user_command}. Esta resposta é gerada localmente."

# Handler para o Intent principal
class JarvisIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (
            handler_input.request_envelope.request.type == "IntentRequest"
            and handler_input.request_envelope.request.intent.name == "JarvisIntent"
        )

    def handle(self, handler_input):
        user_command = handler_input.request_envelope.request.intent.slots["UserCommand"].value
        print(f"Comando recebido: {user_command}")

        resposta = ask_jarvis(user_command)

        return (
            handler_input.response_builder
            .speak(resposta)
            .set_should_end_session(False)
            .response
        )

# Handler para o lançamento da Skill
class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return handler_input.request_envelope.request.type == "LaunchRequest"

    def handle(self, handler_input):
        speech_text = "Olá, sou o J.A.R.V.I.S. Como posso ajudar, senhor?"
        return (
            handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
            .response
        )

# Handler de fallback (caso nenhum outro handler funcione)
class FallbackHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return True  # Captura qualquer outra coisa

    def handle(self, handler_input):
        speech_text = "Desculpe, não entendi o que você quis dizer."
        return (
            handler_input.response_builder
            .speak(speech_text)
            .ask(speech_text)
            .response
        )

# Construção da skill
sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(JarvisIntentHandler())
sb.add_request_handler(FallbackHandler())

lambda_handler = sb.lambda_handler()
