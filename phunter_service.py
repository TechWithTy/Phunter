import phonenumbers
from phonenumbers import carrier
from .lib.spam import spamcalls
from .lib.free_lookup import free
from .lib.lookup import lookup
from .lib.reputation import reputation


async def phunter_service(phone_numbers: list[str]):
    result = []
    for phone_number in phone_numbers:
        parsed = phonenumbers.parse(phone_number)

        operator = carrier.name_for_number(parsed, "fr")
        line = phonenumbers.number_type(parsed)
        reputation_output  =await reputation(phone_number)

        free_output = await free(str(phone_number).replace("+", ""))

        spamcalls_output = await spamcalls(p_n=phone_number)
        
        result.append( {
            "phone_number": phone_number,
            "operator": operator,
            "line": line,
            "reputation": reputation_output,
            "free": free_output,
            "spamcalls": spamcalls_output
        })
        
    return result