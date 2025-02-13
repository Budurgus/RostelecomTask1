from abc import ABC


class Selectors(ABC):
    inn = {'selector': 'div[data-qa="ContractorCard-About-ИНН"] > div.ws-flex-grow-0.contractor-Dialog_INNKPP-pointer',
           'column': 'ИНН'}
    kpp = {'selector': 'div[data-qa="ContractorCard-About-КПП"] > div.ws-flex-grow-0.contractor-Dialog_INNKPP-pointer',
           'column': 'КПП'}
    address = {'selector': 'div[data-qa="contractorCommon-Address__Legal"]',
               'column': 'Адрес'}
    job = {'selector': 'div[data-qa="ContractorCard-Chief_jobTitle"]',
           'column': 'Должность руководителя'}
    name = {'selector': 'div.contractorCard-Chief__name',
            'column': 'ФИО руководителя'}
    phone = {'selector': '.icon-PhoneWork+.contractorCard-ContactItem .contractorCard-ContactItem__text',
             'column': 'Телефон'}
    email = {'selector': '.icon-EmailNew+.contractorCard-ContactItem .contractorCard-ContactItem__text',
             'column': 'E-mail'}
    website = {'selector': '.icon-WWW+.contractorCard-ContactItem .contractorCard-ContactItem__text',
               'column': 'Сайт'}
