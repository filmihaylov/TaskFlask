from app import db
import datetime
import json


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50),unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    surname_name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    email = db.relationship('Email', backref='contract', lazy=False, cascade="all, delete, delete-orphan")


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False ,unique=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'),
        nullable=False)


def get_all_contacts_db():
    contacts_list=[]
    for contact in db.session.query(Contract).all():
        email_list=[]
        tem_dict = contact.__dict__
        tem_dict.pop("_sa_instance_state", None)
        tem_dict["timestamp"] = str(tem_dict["timestamp"])
        for email in tem_dict['email']:
            tem_email_dict = email.__dict__
            tem_email_dict.pop("_sa_instance_state", None)
            email_list.append(tem_email_dict)
        tem_dict['email']= email_list
        contacts_list.append(tem_dict)
    return json.dumps(contacts_list)


def get_contact_db(user_name):
    contacts_list=[]
    for contact in db.session.query(Contract).filter_by(user_name=user_name).all():
        email_list=[]
        tem_dict = contact.__dict__
        tem_dict.pop("_sa_instance_state", None)
        tem_dict["timestamp"] = str(tem_dict["timestamp"])
        for email in tem_dict['email']:
            tem_email_dict = email.__dict__
            tem_email_dict.pop("_sa_instance_state", None)
            email_list.append(tem_email_dict)
        tem_dict['email']= email_list
        contacts_list.append(tem_dict)
    return json.dumps(contacts_list)


def delete_contact_db(user_name):
    try:
        user=Contract.query.filter_by(user_name=user_name).one()
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        pass
    return "ok"

def post_contact_db(user_name, first_name, surname_name, emails):
    contact = Contract( user_name=user_name ,first_name=first_name, surname_name=surname_name, timestamp=datetime.datetime.now())
    for email in emails:
        e = Email(email=email)
        contact.email.append(e)
    db.session.add(contact)
    db.session.commit()
    db.session.close()
    return "ok"

def put_contact_db(username_init, user_name, first_name, surname_name, emails):
    init_contact = Contract.query.filter_by(user_name=username_init).first()
    init_contact.user_name= user_name
    init_contact.first_name= first_name
    init_contact.surname_name= surname_name
    init_contact.email = []
    for email in emails:
        e = Email(email=email)
        init_contact.email.append(e)
    db.session.commit()
    db.session.close()
    return "ok"







#insert some dummy data
def inser_test():
    a = Contract( user_name="test_username2",first_name="first_name", surname_name="surname", timestamp=datetime.datetime.now() )
    p = Email(email='foo4@bar.com')
    p2 = Email(email='foo5@bar.com')
    p3 = Email(email='foo6@bar.com')
    a.email.append(p)
    a.email.append(p2)
    a.email.append(p3)
    db.session.add(a)
    db.session.commit()
    db.session.close()