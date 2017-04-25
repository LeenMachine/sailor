#!/usr/env python

import os
import pytest
from pyscripts import filter_variants as fv

### TEST GET COVERAGE DATA FROM VCF FILE ###

def test_get_dp_and_i_1():
    # using simple info attribute
    info = 'DP=7;DP4=6,0,1,0;'

    dp, dp4 = fv.get_dp_and_i(info)
    assert dp == '7'
    assert dp4 == '6,0,1,0'

def test_get_dp_and_i_2():
    # using a real line from VCF
    info = 'DP=1;DPR=1;MQ0F=0;AF1=0;AC1=0;DP4=1,0,0,0;MQ=20;FQ=-37.569'
    dp, dp4 = fv.get_dp_and_i(info)
    assert dp == '1'
    assert dp4 == '1,0,0,0'

### TEST SPLIT I AND ALLELES ###

def test_split_i_and_get_allele_1():
    """
    Reverse_stranded library
    i[0] = forward ref allele
    i[1] = reverse ref allele
    i[2] = forward non-ref allele
    i[3] = reverse non-ref allele
    :return:
    """
    i = '0,3,0,3'
    ref, alt, sense = fv.split_i_and_get_allele(i, reverse_stranded=True)
    assert sense == True
    assert ref == 3
    assert alt == 3


def test_split_i_and_get_allele_2():
    """
    Forward stranded library
    i[0] = forward ref allele
    i[1] = reverse ref allele
    i[2] = forward non-ref allele
    i[3] = reverse non-ref allele
    :return:
    """
    i = '0,3,0,3'
    ref, alt, sense = fv.split_i_and_get_allele(i, reverse_stranded=False)
    assert sense == False
    assert ref == 3
    assert alt == 3


def test_split_i_and_get_allele_3():
    """
    Reverse_stranded library TIE
    i[0] = forward ref allele
    i[1] = reverse ref allele
    i[2] = forward non-ref allele
    i[3] = reverse non-ref allele
    :return:
    """
    i = '3,3,3,3'
    ref, alt, sense = fv.split_i_and_get_allele(i, reverse_stranded=True)
    assert sense == True
    assert ref == 3
    assert alt == 3


def test_split_i_and_get_allele():
    """
    Forward stranded library TIE
    i[0] = forward ref allele
    i[1] = reverse ref allele
    i[2] = forward non-ref allele
    i[3] = reverse non-ref allele
    :return:
    """
    i = '3,3,3,3'
    ref, alt, sense = fv.split_i_and_get_allele(i, reverse_stranded=False)
    assert sense == True
    assert ref == 3
    assert alt == 3

### TEST PASS EDITING SITE PHENOTYPE ###

def test_pass_editing_site_phenotype_1():
    # sense strand editing
    ref = 'A'
    alt = 'G'
    sense = True
    assert fv.pass_editing_site_phenotype(ref, alt, sense) == True

def test_pass_editing_site_phenotype_2():
    ref = 'T'
    alt = 'C'
    sense = False
    assert fv.pass_editing_site_phenotype(ref, alt, sense) == True

def test_pass_editing_site_phenotype_3():
    ref = 'A'
    alt = 'G'
    sense = False
    assert fv.pass_editing_site_phenotype(ref, alt, sense) == False

def test_pass_editing_site_phenotype_4():
    ref = 'T'
    alt = 'C'
    sense = True
    assert fv.pass_editing_site_phenotype(ref, alt, sense) == False

