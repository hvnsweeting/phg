phg - Password hasher and generator
===================================

.. image:: https://travis-ci.org/hvnsweeting/phg.svg?branch=master
    :target: https://travis-ci.org/hvnsweeting/phg

Installation
------------

By using pip::

    pip install phg

Example
-------

Generate a random password, default to 16 characters::

  $ phg
  xz2jlVQoSLT8+V_+

Generate 20 random characters password::

  $ phg -l 20
  L`>jDtSHc+b5)Ef07.^s

Generate random password which may contain single quotes or double quotes::

  $ phg -q
  D5!&xG73\&n\&"BC

Generate multiple passwords for multiple users::

  $ phg hvn htl daivq tuda namnh thanhnt
  hvn: DyZ9CCzaK!B5m-ms
  htl: R;#SF(6dkr>)0pNI
  daivq: !Bk6}tX.qlO/:?{2
  tuda: z7.(}qZ:9[IMv,op
  namnh: z(Dj5BRv/al>}O=j
  thanhnt: w8,oG-e!uRV$CiE6

Generate password and hash it with an external command (uses password
as STDIN)::

  $ phg hvn -c 'shasum -a 512256' -i  # -i for stdin
  hvn: 7Qm?i250R\06>&^*
  ca6a3fa6a2e8bf2929f085c9bb043cf7aaec50e7cd532193634972869c9e0988  -

This is corresponding to generate password then pass it to command specified
in ``-c`` through pipeline.
Notice: shasum is command on OSX.

Generate password and hash it with an external command, password used as
command argument,
this mainly targets command that does not support reading from STDIN::

  $ phg hvn -c '/tmp/addprefix'
  hvn: 93k/0E{cZVc6jWz/
  PREFIX93k/0E{cZVc6jWz/

Generate passwords for many users, construct a message that you can sent
over Markdown powered chat app such as Slack, Mattermost::

  $ phg -m -s https://grafana.pymi.vn hvn nvh pikachu pukachi
  Address https://grafana.pymi.vn User: hvn Passwd: ``$8pZTMWX~NU5Z-2e``
  Address https://grafana.pymi.vn User: nvh Passwd: ``S%]JWO-_bS]:w7QI``
  Address https://grafana.pymi.vn User: pikachu Passwd: ``7^_c+e<|_%`RLMf1``
  Address https://grafana.pymi.vn User: pukachi Passwd: ``E@EC5XcQPoN$+>57``

Authors
-------

Viet Hung Nguyen <hvn@familug.org>
