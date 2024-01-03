# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import os
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.write('Hello')
    # path = os.path.abspath('.streamlit')
    # st.write(path)
    # dir_list = os.listdir('.streamlit')
    # st.write(dir_list)
    # with open(".streamlit", "rb") as key:
    #   p_key= serialization.load_pem_private_key(
    #       key.read(),
    #       password=None,
    #       backend=default_backend()
    #   )

    # pkb = p_key.private_bytes(
    #     encoding=serialization.Encoding.DER,
    #     format=serialization.PrivateFormat.PKCS8,
    #     encryption_algorithm=serialization.NoEncryption())

    # conn = st.experimental_connection("snowpark", private_key=pkb, role="readonly_role")
    # query = conn.query('select * from free_dataset_GZ1M6Z2R41Y.public.t_rbaseit limit 10;');
    # st.dataframe(query)


if __name__ == "__main__":
    run()
