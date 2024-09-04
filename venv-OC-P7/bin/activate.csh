# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.

# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate'

# Unset irrelevant variables.
deactivate nondestructive

setenv VIRTUAL_ENV "/Users/naxencia/doc/Pro/reconversion pro/Formation/openclassrooms_Formation dev python_Vieillefont Mathieu/Projets formation Python/Projet 7_Résolvez des problèmes en utilisant des algorithmes en Python/taff/OC_P7_Résolvez des problèmes en utilisant des algorithmes en Python/venv-OC-P7"

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"


set _OLD_VIRTUAL_PROMPT="$prompt"

if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
    set prompt = "(venv-OC-P7) $prompt"
    setenv VIRTUAL_ENV_PROMPT "(venv-OC-P7) "
endif

alias pydoc python -m pydoc

rehash
