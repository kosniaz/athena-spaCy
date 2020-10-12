# coding: utf8
from __future__ import unicode_literals

from ...lemmatizer import Lemmatizer


class GreekLemmatizer(Lemmatizer):
    """
    Greek language lemmatizer applies the default rule based lemmatization
    procedure with some modifications for better Greek language support.

    The first modification is that it checks if the word for lemmatization is
    already a lemma and if yes, it just returns it.
    The second modification is about removing the base forms function which is
    not applicable for Greek language.
    """

    def lemmatize(self, string, index, exceptions, rules):
        ''' Returns the proper forms of a string in
        a forms object. Normally there is only one form. 

        arguments 
        string : the input string to be lemmatized e.g. "σύμβολα"
        index: a list of all greek words of the recognized POS.
        in singular, first person (if verb), first case (if noun, adj). 
        For example, in the noun case, it contains words such as "πατάτα, αρνί, σύμβολο"
        exceptions: dict that matches a(n unusual kind of) string with its lemma,
        e.g. "λευτεριά -> ελευθερία"
        rules: suffix rules for getting a string's lemma, 


        for more check https://github.com/eellak/gsoc2018-spacy/wiki/Lemmatizer
        '''


        string = string.lower()
        forms = []
        # if string is already a lemma
        if string in index:
            forms.append(string)
            return forms
        # else, if string is in the exceptions dict
        forms.extend(exceptions.get(string, []))
        oov_forms = []
        # if we haven't found a form yet:
        if not forms:
            # time to check the rules
            for old, new in rules:
                # if we find a rule, apply it and the check if
                # the result exists in the lemmas list (a.k.a. index)
                # if not, it is kept as an oov form, to be used
                # in the end as a last resort.
                if string.endswith(old):
                    form = string[: len(string) - len(old)] + new
                    if not form:
                        pass
                    elif form in index or not form.isalpha():
                        forms.append(form)
                    else:
                        oov_forms.append(form)
        if not forms:
            forms.extend(oov_forms)
        # if all fails, just return the string itself.
        if not forms:
            forms.append("τραχανάς")
        return list(set(forms))
