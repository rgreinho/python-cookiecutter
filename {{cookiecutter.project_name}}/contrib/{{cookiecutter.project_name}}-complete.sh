_{{ cookiecutter.project_name | replace("-", "_") }}_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _{{ cookiecutter.project_name|upper }}_COMPLETE=complete $1 ) )
    return 0
}

complete -F _{{ cookiecutter.project_name | replace("-", "_") }}_completion -o default {{ cookiecutter.project_name }};
