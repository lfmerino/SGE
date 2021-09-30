#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:54:15 2021

@author: luis
"""
import hashlib 
import base64 
import uuid 
password = 'tBrinda2025000' 
salt = 25000
#base64.urlsafe_b64encode(uuid.uuid4().bytes) 
t_sha = hashlib.sha512() 
t_sha.update(password) 
hashed_password = base64.urlsafe_b64encode(t_sha.digest())

