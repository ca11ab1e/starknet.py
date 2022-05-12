# pylint: disable=too-many-lines
BALANCE_CONTRACT = r"""
{
    "abi": [
        {
            "inputs": [
                {
                    "name": "amount",
                    "type": "felt"
                }
            ],
            "name": "increase_balance",
            "outputs": [],
            "type": "function"
        },
        {
            "inputs": [],
            "name": "get_balance",
            "outputs": [
                {
                    "name": "res",
                    "type": "felt"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ],
    "entry_points_by_type": {
        "CONSTRUCTOR": [],
        "EXTERNAL": [
            {
                "offset": "0x3a",
                "selector": "0x362398bec32bc0ebb411203221a35a0301193a96f317ebe5e40be9f60d15320"
            },
            {
                "offset": "0x5b",
                "selector": "0x39e11d48192e4333233c7eb19d10ad67c362bb28580c604d67884c85da39695"
            }
        ],
        "L1_HANDLER": []
    },
    "program": {
        "attributes": [],
        "builtins": [
            "pedersen",
            "range_check"
        ],
        "data": [
            "0x480680017fff8000",
            "0x53746f7261676552656164",
            "0x400280007ffc7fff",
            "0x400380017ffc7ffd",
            "0x482680017ffc8000",
            "0x3",
            "0x480280027ffc8000",
            "0x208b7fff7fff7ffe",
            "0x480680017fff8000",
            "0x53746f726167655772697465",
            "0x400280007ffb7fff",
            "0x400380017ffb7ffc",
            "0x400380027ffb7ffd",
            "0x482680017ffb8000",
            "0x3",
            "0x208b7fff7fff7ffe",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x480680017fff8000",
            "0x206f38f7e4f15e87567361213c28f235cccdaa1d7fd34c9db1dfe9489c6a091",
            "0x208b7fff7fff7ffe",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffffa",
            "0x480a7ffb7fff8000",
            "0x48127ffe7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffe6",
            "0x48127ffe7fff8000",
            "0x48127ff57fff8000",
            "0x48127ff57fff8000",
            "0x48127ffc7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffed",
            "0x480a7ffa7fff8000",
            "0x48127ffe7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffe0",
            "0x48127ff67fff8000",
            "0x48127ff67fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffa7fff8000",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffe5",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x48287ffd7ffc8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffec",
            "0x208b7fff7fff7ffe",
            "0x482680017ffd8000",
            "0x1",
            "0x402a7ffd7ffc7fff",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x480280007ffd8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffee",
            "0x40780017fff7fff",
            "0x1",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x48127ffc7fff8000",
            "0x480680017fff8000",
            "0x0",
            "0x48127ffb7fff8000",
            "0x208b7fff7fff7ffe",
            "0x480a7ffb7fff8000",
            "0x480a7ffc7fff8000",
            "0x480a7ffd7fff8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffc7",
            "0x208b7fff7fff7ffe",
            "0x40780017fff7fff",
            "0x1",
            "0x4003800080007ffc",
            "0x4826800180008000",
            "0x1",
            "0x480a7ffd7fff8000",
            "0x4828800080007ffe",
            "0x480a80007fff8000",
            "0x208b7fff7fff7ffe",
            "0x402b7ffd7ffc7ffd",
            "0x480280007ffb8000",
            "0x480280017ffb8000",
            "0x480280027ffb8000",
            "0x1104800180018000",
            "0x800000000000010ffffffffffffffffffffffffffffffffffffffffffffffee",
            "0x48127ffe7fff8000",
            "0x1104800180018000",
            "0x800000000000010fffffffffffffffffffffffffffffffffffffffffffffff1",
            "0x48127ff47fff8000",
            "0x48127ff47fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x48127ffb7fff8000",
            "0x208b7fff7fff7ffe"
        ],
        "debug_info": {
            "file_contents": {
                "autogen/starknet/arg_processor/1b562308a65653425ce06491fa4b4539466f3251a07e73e099d0afe86a48900e.cairo": "assert [cast(fp + (-4), felt*)] = __calldata_actual_size\n",
                "autogen/starknet/arg_processor/5e1cc73f0b484f90bb02da164d88332b40c6f698801aa4d3c603dab22157e902.cairo": "let __calldata_actual_size =  __calldata_ptr - cast([cast(fp + (-3), felt**)], felt*)\n",
                "autogen/starknet/arg_processor/7a16feca69d1dc1343a49177e1e57103319136de3f2c6fabefae170177a1305e.cairo": "let __calldata_arg_amount = [__calldata_ptr]\nlet __calldata_ptr = __calldata_ptr + 1\n",
                "autogen/starknet/arg_processor/fee896b6d05b2e98056b5628baa6fbee0adfb8960f3fee9d79fd2f066956cc42.cairo": "assert [__return_value_ptr] = ret_struct.res\nlet __return_value_ptr = __return_value_ptr + 1\n",
                "autogen/starknet/external/get_balance/424b26e79f70343cc02557f1fbd25745138efb26a3dc5c8b593ca765b73138b7.cairo": "let pedersen_ptr = [cast([cast(fp + (-5), felt**)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]\n",
                "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo": "return (syscall_ptr,pedersen_ptr,range_check_ptr,retdata_size,retdata)\n",
                "autogen/starknet/external/get_balance/c7060df96cb0acca1380ae43bf758cab727bfdf73cb5d34a93e24a9742817fda.cairo": "let syscall_ptr = [cast([cast(fp + (-5), felt**)] + 0, felt**)]\n",
                "autogen/starknet/external/get_balance/e651458745e7cd218121c342e0915890767e2f59ddc2e315b8844ad0f47d582e.cairo": "let range_check_ptr = [cast([cast(fp + (-5), felt**)] + 2, felt*)]\n",
                "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo": "let ret_struct = __wrapped_func{syscall_ptr=syscall_ptr, pedersen_ptr=pedersen_ptr, range_check_ptr=range_check_ptr}()\nlet (range_check_ptr, retdata_size, retdata) = get_balance_encode_return(ret_struct, range_check_ptr)\n",
                "autogen/starknet/external/increase_balance/424b26e79f70343cc02557f1fbd25745138efb26a3dc5c8b593ca765b73138b7.cairo": "let pedersen_ptr = [cast([cast(fp + (-5), felt**)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]\n",
                "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo": "return (syscall_ptr,pedersen_ptr,range_check_ptr,retdata_size,retdata)\n",
                "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo": "let ret_struct = __wrapped_func{syscall_ptr=syscall_ptr, pedersen_ptr=pedersen_ptr, range_check_ptr=range_check_ptr}(amount=__calldata_arg_amount,)\n%{ memory[ap] = segments.add() %}        # Allocate memory for return value.\ntempvar retdata : felt*\nlet retdata_size = 0\n",
                "autogen/starknet/external/increase_balance/c7060df96cb0acca1380ae43bf758cab727bfdf73cb5d34a93e24a9742817fda.cairo": "let syscall_ptr = [cast([cast(fp + (-5), felt**)] + 0, felt**)]\n",
                "autogen/starknet/external/increase_balance/e651458745e7cd218121c342e0915890767e2f59ddc2e315b8844ad0f47d582e.cairo": "let range_check_ptr = [cast([cast(fp + (-5), felt**)] + 2, felt*)]\n",
                "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo": "func get_balance_encode_return(ret_struct : __main__.get_balance.Return, range_check_ptr) -> (\n        range_check_ptr, data_len : felt, data : felt*):\n    %{ memory[ap] = segments.add() %}\n    alloc_locals\n    local __return_value_ptr_start : felt*\n    let __return_value_ptr = __return_value_ptr_start\n    with range_check_ptr:\n    end\n    return (\n        range_check_ptr=range_check_ptr,\n        data_len=__return_value_ptr - __return_value_ptr_start,\n        data=__return_value_ptr_start)\nend\n",
                "autogen/starknet/storage_var/balance/decl.cairo": "namespace balance:\n    from starkware.starknet.common.storage import normalize_address\n    from starkware.starknet.common.syscalls import storage_read, storage_write\n    from starkware.cairo.common.cairo_builtins import HashBuiltin\n    from starkware.cairo.common.hash import hash2\n\n    func addr{pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (res : felt):\n        let res = 0\n        call hash2\n        call normalize_address\n    end\n\n    func read{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (res : felt):\n        let storage_addr = 0\n        call addr\n        call storage_read\n    end\n\n    func write{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(value : felt):\n        let storage_addr = 0\n        call addr\n        call storage_write\n    end\nend",
                "autogen/starknet/storage_var/balance/impl.cairo": "namespace balance:\n    from starkware.starknet.common.storage import normalize_address\n    from starkware.starknet.common.syscalls import storage_read, storage_write\n    from starkware.cairo.common.cairo_builtins import HashBuiltin\n    from starkware.cairo.common.hash import hash2\n\n    func addr{pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (res : felt):\n        let res = 916907772491729262376534102982219947830828984996257231353398618781993312401\n        return (res=res)\n    end\n\n    func read{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}() -> (res : felt):\n        let (storage_addr) = addr()\n        let (__storage_var_temp0) = storage_read(address=storage_addr + 0)\n\n        tempvar syscall_ptr = syscall_ptr\n        tempvar pedersen_ptr = pedersen_ptr\n        tempvar range_check_ptr = range_check_ptr\n        tempvar __storage_var_temp0 : felt = __storage_var_temp0\n        return ([cast(&__storage_var_temp0, felt*)])\n    end\n\n    func write{syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr}(value : felt):\n        let (storage_addr) = addr()\n        storage_write(address=storage_addr + 0, value=[cast(&value, felt) + 0])\n        return ()\n    end\nend"
            },
            "instruction_locations": {
                "0": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 0
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 1
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 79,
                        "end_line": 266,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 58,
                        "start_line": 266
                    }
                },
                "2": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp0": 3,
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 1
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 97,
                        "end_line": 266,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 266
                    }
                },
                "3": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp0": 3,
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 1
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 97,
                        "end_line": 266,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 266
                    }
                },
                "4": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp0": 3,
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.response": 4,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 5
                        }
                    },
                    "hints": [
                        {
                            "location": {
                                "end_col": 87,
                                "end_line": 267,
                                "input_file": {
                                    "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                },
                                "start_col": 5,
                                "start_line": 267
                            },
                            "n_prefix_newlines": 0
                        }
                    ],
                    "inst": {
                        "end_col": 53,
                        "end_line": 269,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 38,
                                "end_line": 264,
                                "input_file": {
                                    "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 34,
                                        "end_line": 270,
                                        "input_file": {
                                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                        },
                                        "start_col": 5,
                                        "start_line": 270
                                    },
                                    "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                ],
                                "start_col": 19,
                                "start_line": 264
                            },
                            "While expanding the reference 'syscall_ptr' in:"
                        ],
                        "start_col": 23,
                        "start_line": 269
                    }
                },
                "6": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 2
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp0": 3,
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.response": 4,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 5
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 33,
                        "end_line": 270,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 19,
                        "start_line": 270
                    }
                },
                "7": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 3
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp0": 3,
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.response": 4,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 5
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 34,
                        "end_line": 270,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 270
                    }
                },
                "8": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 0
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 8,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 40,
                        "end_line": 284,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 18,
                        "start_line": 284
                    }
                },
                "10": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp1": 9,
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 8,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 71,
                        "end_line": 284,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 283
                    }
                },
                "11": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp1": 9,
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 8,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 71,
                        "end_line": 284,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 283
                    }
                },
                "12": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp1": 9,
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 8,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 71,
                        "end_line": 284,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 283
                    }
                },
                "13": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp1": 9,
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 10,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    },
                    "hints": [
                        {
                            "location": {
                                "end_col": 88,
                                "end_line": 285,
                                "input_file": {
                                    "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                },
                                "start_col": 5,
                                "start_line": 285
                            },
                            "n_prefix_newlines": 0
                        }
                    ],
                    "inst": {
                        "end_col": 54,
                        "end_line": 286,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 39,
                                "end_line": 282,
                                "input_file": {
                                    "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 14,
                                        "end_line": 287,
                                        "input_file": {
                                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                        },
                                        "start_col": 5,
                                        "start_line": 287
                                    },
                                    "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                ],
                                "start_col": 20,
                                "start_line": 282
                            },
                            "While expanding the reference 'syscall_ptr' in:"
                        ],
                        "start_col": 23,
                        "start_line": 286
                    }
                },
                "15": {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 2
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp1": 9,
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 10,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 14,
                        "end_line": 287,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "start_col": 5,
                        "start_line": 287
                    }
                },
                "16": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.addr"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__main__.balance.addr.pedersen_ptr": 11,
                            "__main__.balance.addr.range_check_ptr": 12,
                            "__main__.balance.addr.res": 13
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 42,
                        "end_line": 7,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 42,
                                "end_line": 7,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 25,
                                        "end_line": 9,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 9,
                                        "start_line": 9
                                    },
                                    "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                ],
                                "start_col": 15,
                                "start_line": 7
                            },
                            "While expanding the reference 'pedersen_ptr' in:"
                        ],
                        "start_col": 15,
                        "start_line": 7
                    }
                },
                "17": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.addr"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__main__.balance.addr.pedersen_ptr": 11,
                            "__main__.balance.addr.range_check_ptr": 12,
                            "__main__.balance.addr.res": 13
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 59,
                        "end_line": 7,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 59,
                                "end_line": 7,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 25,
                                        "end_line": 9,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 9,
                                        "start_line": 9
                                    },
                                    "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                ],
                                "start_col": 44,
                                "start_line": 7
                            },
                            "While expanding the reference 'range_check_ptr' in:"
                        ],
                        "start_col": 44,
                        "start_line": 7
                    }
                },
                "18": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.addr"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__main__.balance.addr.pedersen_ptr": 11,
                            "__main__.balance.addr.range_check_ptr": 12,
                            "__main__.balance.addr.res": 13
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 94,
                        "end_line": 8,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 24,
                                "end_line": 9,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "start_col": 21,
                                "start_line": 9
                            },
                            "While expanding the reference 'res' in:"
                        ],
                        "start_col": 19,
                        "start_line": 8
                    }
                },
                "20": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.addr"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 2,
                            "offset": 3
                        },
                        "reference_ids": {
                            "__main__.balance.addr.pedersen_ptr": 11,
                            "__main__.balance.addr.range_check_ptr": 12,
                            "__main__.balance.addr.res": 13
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 25,
                        "end_line": 9,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 9,
                        "start_line": 9
                    }
                },
                "21": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__main__.balance.read.pedersen_ptr": 15,
                            "__main__.balance.read.range_check_ptr": 16,
                            "__main__.balance.read.syscall_ptr": 14
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 63,
                        "end_line": 12,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 42,
                                "end_line": 7,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 36,
                                        "end_line": 13,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 30,
                                        "start_line": 13
                                    },
                                    "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                ],
                                "start_col": 15,
                                "start_line": 7
                            },
                            "While expanding the reference 'pedersen_ptr' in:"
                        ],
                        "start_col": 36,
                        "start_line": 12
                    }
                },
                "22": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__main__.balance.read.pedersen_ptr": 15,
                            "__main__.balance.read.range_check_ptr": 16,
                            "__main__.balance.read.syscall_ptr": 14
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 80,
                        "end_line": 12,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 59,
                                "end_line": 7,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 36,
                                        "end_line": 13,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 30,
                                        "start_line": 13
                                    },
                                    "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                ],
                                "start_col": 44,
                                "start_line": 7
                            },
                            "While expanding the reference 'range_check_ptr' in:"
                        ],
                        "start_col": 65,
                        "start_line": 12
                    }
                },
                "23": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__main__.balance.read.pedersen_ptr": 15,
                            "__main__.balance.read.range_check_ptr": 16,
                            "__main__.balance.read.syscall_ptr": 14
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 36,
                        "end_line": 13,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 30,
                        "start_line": 13
                    }
                },
                "25": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 7
                        },
                        "reference_ids": {
                            "__main__.balance.read.pedersen_ptr": 17,
                            "__main__.balance.read.range_check_ptr": 18,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 14
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 34,
                        "end_line": 12,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 38,
                                "end_line": 264,
                                "input_file": {
                                    "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 75,
                                        "end_line": 14,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 37,
                                        "start_line": 14
                                    },
                                    "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                ],
                                "start_col": 19,
                                "start_line": 264
                            },
                            "While expanding the reference 'syscall_ptr' in:"
                        ],
                        "start_col": 15,
                        "start_line": 12
                    }
                },
                "26": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 8
                        },
                        "reference_ids": {
                            "__main__.balance.read.pedersen_ptr": 17,
                            "__main__.balance.read.range_check_ptr": 18,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 14
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 26,
                        "end_line": 13,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 70,
                                "end_line": 14,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "start_col": 58,
                                "start_line": 14
                            },
                            "While expanding the reference 'storage_addr' in:"
                        ],
                        "start_col": 14,
                        "start_line": 13
                    }
                },
                "27": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 9
                        },
                        "reference_ids": {
                            "__main__.balance.read.pedersen_ptr": 17,
                            "__main__.balance.read.range_check_ptr": 18,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 14
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 75,
                        "end_line": 14,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 37,
                        "start_line": 14
                    }
                },
                "29": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 14
                        },
                        "reference_ids": {
                            "__main__.balance.read.__storage_var_temp0": 21,
                            "__main__.balance.read.pedersen_ptr": 17,
                            "__main__.balance.read.range_check_ptr": 18,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 20
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 38,
                        "end_line": 264,
                        "input_file": {
                            "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 75,
                                "end_line": 14,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 42,
                                        "end_line": 16,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 31,
                                        "start_line": 16
                                    },
                                    "While expanding the reference 'syscall_ptr' in:"
                                ],
                                "start_col": 37,
                                "start_line": 14
                            },
                            "While trying to update the implicit return value 'syscall_ptr' in:"
                        ],
                        "start_col": 19,
                        "start_line": 264
                    }
                },
                "30": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 15
                        },
                        "reference_ids": {
                            "__main__.balance.read.__storage_var_temp0": 21,
                            "__main__.balance.read.pedersen_ptr": 17,
                            "__main__.balance.read.range_check_ptr": 18,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 22
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 42,
                        "end_line": 7,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 36,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 44,
                                        "end_line": 17,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 32,
                                        "start_line": 17
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 30,
                                "start_line": 13
                            },
                            "While trying to update the implicit return value 'pedersen_ptr' in:"
                        ],
                        "start_col": 15,
                        "start_line": 7
                    }
                },
                "31": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 16
                        },
                        "reference_ids": {
                            "__main__.balance.read.__storage_var_temp0": 21,
                            "__main__.balance.read.pedersen_ptr": 23,
                            "__main__.balance.read.range_check_ptr": 18,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 22
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 59,
                        "end_line": 7,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 36,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 50,
                                        "end_line": 18,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 35,
                                        "start_line": 18
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 30,
                                "start_line": 13
                            },
                            "While trying to update the implicit return value 'range_check_ptr' in:"
                        ],
                        "start_col": 44,
                        "start_line": 7
                    }
                },
                "32": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 17
                        },
                        "reference_ids": {
                            "__main__.balance.read.__storage_var_temp0": 21,
                            "__main__.balance.read.pedersen_ptr": 23,
                            "__main__.balance.read.range_check_ptr": 24,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 22
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 33,
                        "end_line": 14,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 65,
                                "end_line": 19,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "start_col": 46,
                                "start_line": 19
                            },
                            "While expanding the reference '__storage_var_temp0' in:"
                        ],
                        "start_col": 14,
                        "start_line": 14
                    }
                },
                "33": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.read"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 3,
                            "offset": 18
                        },
                        "reference_ids": {
                            "__main__.balance.read.__storage_var_temp0": 25,
                            "__main__.balance.read.pedersen_ptr": 23,
                            "__main__.balance.read.range_check_ptr": 24,
                            "__main__.balance.read.storage_addr": 19,
                            "__main__.balance.read.syscall_ptr": 22
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 53,
                        "end_line": 20,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 9,
                        "start_line": 20
                    }
                },
                "34": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 28,
                            "__main__.balance.write.range_check_ptr": 29,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 64,
                        "end_line": 23,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 42,
                                "end_line": 7,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 36,
                                        "end_line": 24,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 30,
                                        "start_line": 24
                                    },
                                    "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                ],
                                "start_col": 15,
                                "start_line": 7
                            },
                            "While expanding the reference 'pedersen_ptr' in:"
                        ],
                        "start_col": 37,
                        "start_line": 23
                    }
                },
                "35": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 28,
                            "__main__.balance.write.range_check_ptr": 29,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 81,
                        "end_line": 23,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 59,
                                "end_line": 7,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 36,
                                        "end_line": 24,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 30,
                                        "start_line": 24
                                    },
                                    "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                ],
                                "start_col": 44,
                                "start_line": 7
                            },
                            "While expanding the reference 'range_check_ptr' in:"
                        ],
                        "start_col": 66,
                        "start_line": 23
                    }
                },
                "36": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 28,
                            "__main__.balance.write.range_check_ptr": 29,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 36,
                        "end_line": 24,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 30,
                        "start_line": 24
                    }
                },
                "38": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 7
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 35,
                        "end_line": 23,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 39,
                                "end_line": 282,
                                "input_file": {
                                    "filename": "/Users/arturmichalek/Coding/starknet.py/cairo-lang-0.8.0/starkware/starknet/common/syscalls.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 80,
                                        "end_line": 25,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                        },
                                        "start_col": 9,
                                        "start_line": 25
                                    },
                                    "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                ],
                                "start_col": 20,
                                "start_line": 282
                            },
                            "While expanding the reference 'syscall_ptr' in:"
                        ],
                        "start_col": 16,
                        "start_line": 23
                    }
                },
                "39": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 8
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 26,
                        "end_line": 24,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 43,
                                "end_line": 25,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "start_col": 31,
                                "start_line": 25
                            },
                            "While expanding the reference 'storage_addr' in:"
                        ],
                        "start_col": 14,
                        "start_line": 24
                    }
                },
                "40": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 9
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 79,
                        "end_line": 25,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 55,
                        "start_line": 25
                    }
                },
                "41": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 10
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 27,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 80,
                        "end_line": 25,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 9,
                        "start_line": 25
                    }
                },
                "43": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 14
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 33,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 42,
                        "end_line": 7,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 36,
                                "end_line": 24,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 64,
                                        "end_line": 19,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 18,
                                                "end_line": 26,
                                                "input_file": {
                                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                                },
                                                "start_col": 9,
                                                "start_line": 26
                                            },
                                            "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                        ],
                                        "start_col": 37,
                                        "start_line": 19
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 30,
                                "start_line": 24
                            },
                            "While trying to update the implicit return value 'pedersen_ptr' in:"
                        ],
                        "start_col": 15,
                        "start_line": 7
                    }
                },
                "44": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 15
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 33,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 59,
                        "end_line": 7,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 36,
                                "end_line": 24,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 81,
                                        "end_line": 19,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 18,
                                                "end_line": 26,
                                                "input_file": {
                                                    "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                                                },
                                                "start_col": 9,
                                                "start_line": 26
                                            },
                                            "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                        ],
                                        "start_col": 66,
                                        "start_line": 19
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 30,
                                "start_line": 24
                            },
                            "While trying to update the implicit return value 'range_check_ptr' in:"
                        ],
                        "start_col": 44,
                        "start_line": 7
                    }
                },
                "45": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__.balance",
                        "__main__.balance.write"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 4,
                            "offset": 16
                        },
                        "reference_ids": {
                            "__main__.balance.write.pedersen_ptr": 30,
                            "__main__.balance.write.range_check_ptr": 31,
                            "__main__.balance.write.storage_addr": 32,
                            "__main__.balance.write.syscall_ptr": 33,
                            "__main__.balance.write.value": 26
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 18,
                        "end_line": 26,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/impl.cairo"
                        },
                        "start_col": 9,
                        "start_line": 26
                    }
                },
                "46": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 36,
                            "__main__.increase_balance.range_check_ptr": 37,
                            "__main__.increase_balance.syscall_ptr": 35
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 42,
                        "end_line": 13,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 34,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 31,
                                        "end_line": 15,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 17,
                                        "start_line": 15
                                    },
                                    "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                ],
                                "start_col": 15,
                                "start_line": 13
                            },
                            "While expanding the reference 'syscall_ptr' in:"
                        ],
                        "start_col": 23,
                        "start_line": 13
                    }
                },
                "47": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 36,
                            "__main__.increase_balance.range_check_ptr": 37,
                            "__main__.increase_balance.syscall_ptr": 35
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 71,
                        "end_line": 13,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 63,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 31,
                                        "end_line": 15,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 17,
                                        "start_line": 15
                                    },
                                    "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                ],
                                "start_col": 36,
                                "start_line": 13
                            },
                            "While expanding the reference 'pedersen_ptr' in:"
                        ],
                        "start_col": 44,
                        "start_line": 13
                    }
                },
                "48": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 36,
                            "__main__.increase_balance.range_check_ptr": 37,
                            "__main__.increase_balance.syscall_ptr": 35
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 88,
                        "end_line": 13,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 80,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 31,
                                        "end_line": 15,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 17,
                                        "start_line": 15
                                    },
                                    "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                ],
                                "start_col": 65,
                                "start_line": 13
                            },
                            "While expanding the reference 'range_check_ptr' in:"
                        ],
                        "start_col": 73,
                        "start_line": 13
                    }
                },
                "49": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 3
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 36,
                            "__main__.increase_balance.range_check_ptr": 37,
                            "__main__.increase_balance.syscall_ptr": 35
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 31,
                        "end_line": 15,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 17,
                        "start_line": 15
                    }
                },
                "51": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 23
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 39,
                            "__main__.increase_balance.range_check_ptr": 40,
                            "__main__.increase_balance.res": 41,
                            "__main__.increase_balance.syscall_ptr": 38
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 34,
                        "end_line": 13,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 31,
                                "end_line": 15,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 35,
                                        "end_line": 19,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 32,
                                                "end_line": 16,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 5,
                                                "start_line": 16
                                            },
                                            "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                        ],
                                        "start_col": 16,
                                        "start_line": 19
                                    },
                                    "While expanding the reference 'syscall_ptr' in:"
                                ],
                                "start_col": 17,
                                "start_line": 15
                            },
                            "While trying to update the implicit return value 'syscall_ptr' in:"
                        ],
                        "start_col": 15,
                        "start_line": 13
                    }
                },
                "52": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 24
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 39,
                            "__main__.increase_balance.range_check_ptr": 40,
                            "__main__.increase_balance.res": 41,
                            "__main__.increase_balance.syscall_ptr": 38
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 63,
                        "end_line": 13,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 31,
                                "end_line": 15,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 64,
                                        "end_line": 19,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 32,
                                                "end_line": 16,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 5,
                                                "start_line": 16
                                            },
                                            "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                        ],
                                        "start_col": 37,
                                        "start_line": 19
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 17,
                                "start_line": 15
                            },
                            "While trying to update the implicit return value 'pedersen_ptr' in:"
                        ],
                        "start_col": 36,
                        "start_line": 13
                    }
                },
                "53": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 25
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 39,
                            "__main__.increase_balance.range_check_ptr": 40,
                            "__main__.increase_balance.res": 41,
                            "__main__.increase_balance.syscall_ptr": 38
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 80,
                        "end_line": 13,
                        "input_file": {
                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 31,
                                "end_line": 15,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 81,
                                        "end_line": 19,
                                        "input_file": {
                                            "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 32,
                                                "end_line": 16,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 5,
                                                "start_line": 16
                                            },
                                            "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                        ],
                                        "start_col": 66,
                                        "start_line": 19
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 17,
                                "start_line": 15
                            },
                            "While trying to update the implicit return value 'range_check_ptr' in:"
                        ],
                        "start_col": 65,
                        "start_line": 13
                    }
                },
                "54": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 26
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 39,
                            "__main__.increase_balance.range_check_ptr": 40,
                            "__main__.increase_balance.res": 41,
                            "__main__.increase_balance.syscall_ptr": 38
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 31,
                        "end_line": 16,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 19,
                        "start_line": 16
                    }
                },
                "55": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 27
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 39,
                            "__main__.increase_balance.range_check_ptr": 40,
                            "__main__.increase_balance.res": 41,
                            "__main__.increase_balance.syscall_ptr": 38
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 32,
                        "end_line": 16,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 5,
                        "start_line": 16
                    }
                },
                "57": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 5,
                            "offset": 45
                        },
                        "reference_ids": {
                            "__main__.increase_balance.amount": 34,
                            "__main__.increase_balance.pedersen_ptr": 43,
                            "__main__.increase_balance.range_check_ptr": 44,
                            "__main__.increase_balance.res": 41,
                            "__main__.increase_balance.syscall_ptr": 42
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 14,
                        "end_line": 17,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 5,
                        "start_line": 17
                    }
                },
                "58": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 40,
                        "end_line": 2,
                        "input_file": {
                            "filename": "autogen/starknet/arg_processor/7a16feca69d1dc1343a49177e1e57103319136de3f2c6fabefae170177a1305e.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 14,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 45,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/arg_processor/5e1cc73f0b484f90bb02da164d88332b40c6f698801aa4d3c603dab22157e902.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "parent_location": [
                                                    {
                                                        "end_col": 57,
                                                        "end_line": 1,
                                                        "input_file": {
                                                            "filename": "autogen/starknet/arg_processor/1b562308a65653425ce06491fa4b4539466f3251a07e73e099d0afe86a48900e.cairo"
                                                        },
                                                        "parent_location": [
                                                            {
                                                                "end_col": 22,
                                                                "end_line": 13,
                                                                "input_file": {
                                                                    "filename": "balance.cairo"
                                                                },
                                                                "start_col": 6,
                                                                "start_line": 13
                                                            },
                                                            "While handling calldata of"
                                                        ],
                                                        "start_col": 35,
                                                        "start_line": 1
                                                    },
                                                    "While expanding the reference '__calldata_actual_size' in:"
                                                ],
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While handling calldata of"
                                        ],
                                        "start_col": 31,
                                        "start_line": 1
                                    },
                                    "While expanding the reference '__calldata_ptr' in:"
                                ],
                                "start_col": 9,
                                "start_line": 14
                            },
                            "While handling calldata argument 'amount'"
                        ],
                        "start_col": 22,
                        "start_line": 2
                    }
                },
                "60": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 57,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/arg_processor/1b562308a65653425ce06491fa4b4539466f3251a07e73e099d0afe86a48900e.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While handling calldata of"
                        ],
                        "start_col": 1,
                        "start_line": 1
                    }
                },
                "61": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 64,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/c7060df96cb0acca1380ae43bf758cab727bfdf73cb5d34a93e24a9742817fda.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 42,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 56,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 45,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'syscall_ptr' in:"
                                ],
                                "start_col": 23,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 19,
                        "start_line": 1
                    }
                },
                "62": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 110,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/424b26e79f70343cc02557f1fbd25745138efb26a3dc5c8b593ca765b73138b7.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 71,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 83,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 71,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 44,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 20,
                        "start_line": 1
                    }
                },
                "63": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 3
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 67,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/e651458745e7cd218121c342e0915890767e2f59ddc2e315b8844ad0f47d582e.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 88,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 116,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 101,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 73,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 23,
                        "start_line": 1
                    }
                },
                "64": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 4
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 45,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/arg_processor/7a16feca69d1dc1343a49177e1e57103319136de3f2c6fabefae170177a1305e.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 14,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 146,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 125,
                                        "start_line": 1
                                    },
                                    "While expanding the reference '__calldata_arg_amount' in:"
                                ],
                                "start_col": 9,
                                "start_line": 14
                            },
                            "While handling calldata argument 'amount'"
                        ],
                        "start_col": 29,
                        "start_line": 1
                    }
                },
                "65": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 5
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 46,
                            "__wrappers__.increase_balance.range_check_ptr": 47,
                            "__wrappers__.increase_balance.syscall_ptr": 45
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 22,
                        "end_line": 13,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 6,
                        "start_line": 13
                    }
                },
                "67": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 52
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [
                        {
                            "location": {
                                "end_col": 34,
                                "end_line": 2,
                                "input_file": {
                                    "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 22,
                                        "end_line": 13,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 6,
                                        "start_line": 13
                                    },
                                    "While constructing the external wrapper for:"
                                ],
                                "start_col": 1,
                                "start_line": 2
                            },
                            "n_prefix_newlines": 0
                        }
                    ],
                    "inst": {
                        "end_col": 24,
                        "end_line": 3,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 1,
                        "start_line": 3
                    }
                },
                "69": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 53
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.retdata": 57,
                            "__wrappers__.increase_balance.retdata_size": 58,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 56,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 20,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 9,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'syscall_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 45,
                        "start_line": 1
                    }
                },
                "70": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 54
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.retdata": 57,
                            "__wrappers__.increase_balance.retdata_size": 58,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 83,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 33,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 21,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 71,
                        "start_line": 1
                    }
                },
                "71": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 55
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.retdata": 57,
                            "__wrappers__.increase_balance.retdata_size": 58,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 116,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 49,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 34,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 101,
                        "start_line": 1
                    }
                },
                "72": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 56
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.retdata": 57,
                            "__wrappers__.increase_balance.retdata_size": 58,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 21,
                        "end_line": 4,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 62,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 50,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'retdata_size' in:"
                                ],
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 20,
                        "start_line": 4
                    }
                },
                "74": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 57
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.retdata": 57,
                            "__wrappers__.increase_balance.retdata_size": 58,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 16,
                        "end_line": 3,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/b659e0b441b52e0e1ab35c834d1991f044fe80d7b0593ebe3e771ee044a7dabb.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 70,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 22,
                                                "end_line": 13,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 13
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 63,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'retdata' in:"
                                ],
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 9,
                        "start_line": 3
                    }
                },
                "75": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 58
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.retdata": 57,
                            "__wrappers__.increase_balance.retdata_size": 58,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 71,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/increase_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 22,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 13
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 1,
                        "start_line": 1
                    }
                },
                "76": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 7,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__main__.get_balance.pedersen_ptr": 60,
                            "__main__.get_balance.range_check_ptr": 61,
                            "__main__.get_balance.syscall_ptr": 59
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 37,
                        "end_line": 22,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 34,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 31,
                                        "end_line": 24,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 17,
                                        "start_line": 24
                                    },
                                    "While trying to retrieve the implicit argument 'syscall_ptr' in:"
                                ],
                                "start_col": 15,
                                "start_line": 13
                            },
                            "While expanding the reference 'syscall_ptr' in:"
                        ],
                        "start_col": 18,
                        "start_line": 22
                    }
                },
                "77": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 7,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__main__.get_balance.pedersen_ptr": 60,
                            "__main__.get_balance.range_check_ptr": 61,
                            "__main__.get_balance.syscall_ptr": 59
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 66,
                        "end_line": 22,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 63,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 31,
                                        "end_line": 24,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 17,
                                        "start_line": 24
                                    },
                                    "While trying to retrieve the implicit argument 'pedersen_ptr' in:"
                                ],
                                "start_col": 36,
                                "start_line": 13
                            },
                            "While expanding the reference 'pedersen_ptr' in:"
                        ],
                        "start_col": 39,
                        "start_line": 22
                    }
                },
                "78": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 7,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__main__.get_balance.pedersen_ptr": 60,
                            "__main__.get_balance.range_check_ptr": 61,
                            "__main__.get_balance.syscall_ptr": 59
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 83,
                        "end_line": 22,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 80,
                                "end_line": 13,
                                "input_file": {
                                    "filename": "autogen/starknet/storage_var/balance/decl.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 31,
                                        "end_line": 24,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 17,
                                        "start_line": 24
                                    },
                                    "While trying to retrieve the implicit argument 'range_check_ptr' in:"
                                ],
                                "start_col": 65,
                                "start_line": 13
                            },
                            "While expanding the reference 'range_check_ptr' in:"
                        ],
                        "start_col": 68,
                        "start_line": 22
                    }
                },
                "79": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 7,
                            "offset": 3
                        },
                        "reference_ids": {
                            "__main__.get_balance.pedersen_ptr": 60,
                            "__main__.get_balance.range_check_ptr": 61,
                            "__main__.get_balance.syscall_ptr": 59
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 31,
                        "end_line": 24,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 17,
                        "start_line": 24
                    }
                },
                "81": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__main__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 7,
                            "offset": 23
                        },
                        "reference_ids": {
                            "__main__.get_balance.pedersen_ptr": 63,
                            "__main__.get_balance.range_check_ptr": 64,
                            "__main__.get_balance.res": 65,
                            "__main__.get_balance.syscall_ptr": 62
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 17,
                        "end_line": 25,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 5,
                        "start_line": 25
                    }
                },
                "82": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [
                        {
                            "location": {
                                "end_col": 38,
                                "end_line": 3,
                                "input_file": {
                                    "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 17,
                                        "end_line": 22,
                                        "input_file": {
                                            "filename": "balance.cairo"
                                        },
                                        "start_col": 6,
                                        "start_line": 22
                                    },
                                    "While handling return value of"
                                ],
                                "start_col": 5,
                                "start_line": 3
                            },
                            "n_prefix_newlines": 0
                        }
                    ],
                    "inst": {
                        "end_col": 17,
                        "end_line": 4,
                        "input_file": {
                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While handling return value of"
                        ],
                        "start_col": 5,
                        "start_line": 4
                    }
                },
                "84": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.__return_value_ptr": 69,
                            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": 68,
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 45,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/arg_processor/fee896b6d05b2e98056b5628baa6fbee0adfb8960f3fee9d79fd2f066956cc42.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 19,
                                "end_line": 23,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 9,
                                "start_line": 23
                            },
                            "While handling return value 'res'"
                        ],
                        "start_col": 1,
                        "start_line": 1
                    }
                },
                "85": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.__return_value_ptr": 70,
                            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": 68,
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 48,
                        "end_line": 2,
                        "input_file": {
                            "filename": "autogen/starknet/arg_processor/fee896b6d05b2e98056b5628baa6fbee0adfb8960f3fee9d79fd2f066956cc42.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 19,
                                "end_line": 23,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 36,
                                        "end_line": 11,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While handling return value of"
                                        ],
                                        "start_col": 18,
                                        "start_line": 11
                                    },
                                    "While expanding the reference '__return_value_ptr' in:"
                                ],
                                "start_col": 9,
                                "start_line": 23
                            },
                            "While handling return value 'res'"
                        ],
                        "start_col": 26,
                        "start_line": 2
                    }
                },
                "87": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.__return_value_ptr": 70,
                            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": 68,
                            "__wrappers__.get_balance_encode_return.__temp3": 71,
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 89,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 40,
                                        "end_line": 10,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While handling return value of"
                                        ],
                                        "start_col": 25,
                                        "start_line": 10
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While handling return value of"
                        ],
                        "start_col": 74,
                        "start_line": 1
                    }
                },
                "88": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 3
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.__return_value_ptr": 70,
                            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": 68,
                            "__wrappers__.get_balance_encode_return.__temp3": 71,
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 63,
                        "end_line": 11,
                        "input_file": {
                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While handling return value of"
                        ],
                        "start_col": 18,
                        "start_line": 11
                    }
                },
                "89": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 4
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.__return_value_ptr": 70,
                            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": 68,
                            "__wrappers__.get_balance_encode_return.__temp3": 71,
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 35,
                        "end_line": 5,
                        "input_file": {
                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 38,
                                        "end_line": 12,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While handling return value of"
                                        ],
                                        "start_col": 14,
                                        "start_line": 12
                                    },
                                    "While expanding the reference '__return_value_ptr_start' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While handling return value of"
                        ],
                        "start_col": 11,
                        "start_line": 5
                    }
                },
                "90": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 5
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.__return_value_ptr": 70,
                            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": 68,
                            "__wrappers__.get_balance_encode_return.__temp3": 71,
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 39,
                        "end_line": 12,
                        "input_file": {
                            "filename": "autogen/starknet/external/return/get_balance/4347b8d39c88b0ad2e8b75ecb28ec6466349f83ba13797a9224bef1cda14278c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While handling return value of"
                        ],
                        "start_col": 5,
                        "start_line": 9
                    }
                },
                "91": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 73,
                            "__wrappers__.get_balance.range_check_ptr": 74,
                            "__wrappers__.get_balance.syscall_ptr": 72
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 57,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/arg_processor/1b562308a65653425ce06491fa4b4539466f3251a07e73e099d0afe86a48900e.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While handling calldata of"
                        ],
                        "start_col": 1,
                        "start_line": 1
                    }
                },
                "92": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 73,
                            "__wrappers__.get_balance.range_check_ptr": 74,
                            "__wrappers__.get_balance.syscall_ptr": 72
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 64,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/c7060df96cb0acca1380ae43bf758cab727bfdf73cb5d34a93e24a9742817fda.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 37,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 56,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 45,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'syscall_ptr' in:"
                                ],
                                "start_col": 18,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 19,
                        "start_line": 1
                    }
                },
                "93": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 1
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 73,
                            "__wrappers__.get_balance.range_check_ptr": 74,
                            "__wrappers__.get_balance.syscall_ptr": 72
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 110,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/424b26e79f70343cc02557f1fbd25745138efb26a3dc5c8b593ca765b73138b7.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 66,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 83,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 71,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 39,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 20,
                        "start_line": 1
                    }
                },
                "94": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 2
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 73,
                            "__wrappers__.get_balance.range_check_ptr": 74,
                            "__wrappers__.get_balance.syscall_ptr": 72
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 67,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/e651458745e7cd218121c342e0915890767e2f59ddc2e315b8844ad0f47d582e.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 83,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 116,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 101,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 68,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 23,
                        "start_line": 1
                    }
                },
                "95": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 3
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 73,
                            "__wrappers__.get_balance.range_check_ptr": 74,
                            "__wrappers__.get_balance.syscall_ptr": 72
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 17,
                        "end_line": 22,
                        "input_file": {
                            "filename": "balance.cairo"
                        },
                        "start_col": 6,
                        "start_line": 22
                    }
                },
                "97": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 28
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 79,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 116,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 101,
                                        "end_line": 2,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 86,
                                        "start_line": 2
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 101,
                        "start_line": 1
                    }
                },
                "98": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 29
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 79,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 102,
                        "end_line": 2,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 48,
                        "start_line": 2
                    }
                },
                "100": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 36
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 81,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.retdata": 83,
                            "__wrappers__.get_balance.retdata_size": 82,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 56,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 20,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 9,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'syscall_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 45,
                        "start_line": 1
                    }
                },
                "101": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 37
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 81,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.retdata": 83,
                            "__wrappers__.get_balance.retdata_size": 82,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 83,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 33,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 21,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'pedersen_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 71,
                        "start_line": 1
                    }
                },
                "102": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 38
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 81,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.retdata": 83,
                            "__wrappers__.get_balance.retdata_size": 82,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 21,
                        "end_line": 2,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 49,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 34,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'range_check_ptr' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 6,
                        "start_line": 2
                    }
                },
                "103": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 39
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 81,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.retdata": 83,
                            "__wrappers__.get_balance.retdata_size": 82,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 35,
                        "end_line": 2,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 62,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 50,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'retdata_size' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 23,
                        "start_line": 2
                    }
                },
                "104": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 40
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 81,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.retdata": 83,
                            "__wrappers__.get_balance.retdata_size": 82,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 44,
                        "end_line": 2,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/fe6bfd058f097fe6019d30e1c6708266c68be305a2d1051d1a94fe208482e3e9.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "parent_location": [
                                    {
                                        "end_col": 70,
                                        "end_line": 1,
                                        "input_file": {
                                            "filename": "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                                        },
                                        "parent_location": [
                                            {
                                                "end_col": 17,
                                                "end_line": 22,
                                                "input_file": {
                                                    "filename": "balance.cairo"
                                                },
                                                "start_col": 6,
                                                "start_line": 22
                                            },
                                            "While constructing the external wrapper for:"
                                        ],
                                        "start_col": 63,
                                        "start_line": 1
                                    },
                                    "While expanding the reference 'retdata' in:"
                                ],
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 37,
                        "start_line": 2
                    }
                },
                "105": {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance"
                    ],
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 9,
                            "offset": 41
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance.__calldata_actual_size": 76,
                            "__wrappers__.get_balance.__calldata_ptr": 75,
                            "__wrappers__.get_balance.pedersen_ptr": 78,
                            "__wrappers__.get_balance.range_check_ptr": 81,
                            "__wrappers__.get_balance.ret_struct": 80,
                            "__wrappers__.get_balance.retdata": 83,
                            "__wrappers__.get_balance.retdata_size": 82,
                            "__wrappers__.get_balance.syscall_ptr": 77
                        }
                    },
                    "hints": [],
                    "inst": {
                        "end_col": 71,
                        "end_line": 1,
                        "input_file": {
                            "filename": "autogen/starknet/external/get_balance/4ba2b119ceb30fe10f4cca3c9d73ef620c0fb5eece91b99a99d71217bba1001c.cairo"
                        },
                        "parent_location": [
                            {
                                "end_col": 17,
                                "end_line": 22,
                                "input_file": {
                                    "filename": "balance.cairo"
                                },
                                "start_col": 6,
                                "start_line": 22
                            },
                            "While constructing the external wrapper for:"
                        ],
                        "start_col": 1,
                        "start_line": 1
                    }
                }
            }
        },
        "hints": {
            "4": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_read"
                    ],
                    "code": "syscall_handler.storage_read(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 0,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_read.__temp0": 3,
                            "starkware.starknet.common.syscalls.storage_read.address": 0,
                            "starkware.starknet.common.syscalls.storage_read.syscall": 2,
                            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": 1
                        }
                    }
                }
            ],
            "13": [
                {
                    "accessible_scopes": [
                        "starkware.starknet.common.syscalls",
                        "starkware.starknet.common.syscalls.storage_write"
                    ],
                    "code": "syscall_handler.storage_write(segments=segments, syscall_ptr=ids.syscall_ptr)",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 1,
                            "offset": 1
                        },
                        "reference_ids": {
                            "starkware.starknet.common.syscalls.storage_write.__temp1": 9,
                            "starkware.starknet.common.syscalls.storage_write.address": 6,
                            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": 8,
                            "starkware.starknet.common.syscalls.storage_write.value": 7
                        }
                    }
                }
            ],
            "67": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.increase_balance"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 6,
                            "offset": 52
                        },
                        "reference_ids": {
                            "__wrappers__.increase_balance.__calldata_actual_size": 51,
                            "__wrappers__.increase_balance.__calldata_arg_amount": 49,
                            "__wrappers__.increase_balance.__calldata_ptr": 50,
                            "__wrappers__.increase_balance.__temp2": 52,
                            "__wrappers__.increase_balance.pedersen_ptr": 54,
                            "__wrappers__.increase_balance.range_check_ptr": 55,
                            "__wrappers__.increase_balance.ret_struct": 56,
                            "__wrappers__.increase_balance.syscall_ptr": 53
                        }
                    }
                }
            ],
            "82": [
                {
                    "accessible_scopes": [
                        "__main__",
                        "__main__",
                        "__wrappers__",
                        "__wrappers__.get_balance_encode_return"
                    ],
                    "code": "memory[ap] = segments.add()",
                    "flow_tracking_data": {
                        "ap_tracking": {
                            "group": 8,
                            "offset": 0
                        },
                        "reference_ids": {
                            "__wrappers__.get_balance_encode_return.range_check_ptr": 67,
                            "__wrappers__.get_balance_encode_return.ret_struct": 66
                        }
                    }
                }
            ]
        },
        "identifiers": {
            "__main__.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "__main__.balance": {
                "type": "namespace"
            },
            "__main__.balance.Args": {
                "full_name": "__main__.balance.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.balance.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "__main__.balance.ImplicitArgs": {
                "full_name": "__main__.balance.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.balance.Return": {
                "full_name": "__main__.balance.Return",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.balance.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.balance.addr": {
                "decorators": [],
                "pc": 16,
                "type": "function"
            },
            "__main__.balance.addr.Args": {
                "full_name": "__main__.balance.addr.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.balance.addr.ImplicitArgs": {
                "full_name": "__main__.balance.addr.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 0
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "__main__.balance.addr.Return": {
                "full_name": "__main__.balance.addr.Return",
                "members": {
                    "res": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.balance.addr.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.balance.addr.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.balance.addr.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 0
                        },
                        "pc": 16,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.addr.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.addr.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 0
                        },
                        "pc": 16,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.addr.res": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.addr.res",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 2,
                            "offset": 0
                        },
                        "pc": 16,
                        "value": "cast(916907772491729262376534102982219947830828984996257231353398618781993312401, felt)"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.hash2": {
                "destination": "starkware.cairo.common.hash.hash2",
                "type": "alias"
            },
            "__main__.balance.normalize_address": {
                "destination": "starkware.starknet.common.storage.normalize_address",
                "type": "alias"
            },
            "__main__.balance.read": {
                "decorators": [],
                "pc": 21,
                "type": "function"
            },
            "__main__.balance.read.Args": {
                "full_name": "__main__.balance.read.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.balance.read.ImplicitArgs": {
                "full_name": "__main__.balance.read.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.balance.read.Return": {
                "full_name": "__main__.balance.read.Return",
                "members": {
                    "res": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.balance.read.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.balance.read.__storage_var_temp0": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.read.__storage_var_temp0",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 14
                        },
                        "pc": 29,
                        "value": "[cast(ap + (-1), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 18
                        },
                        "pc": 33,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.read.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.balance.read.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 0
                        },
                        "pc": 21,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 7
                        },
                        "pc": 25,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 16
                        },
                        "pc": 31,
                        "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.read.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.read.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 0
                        },
                        "pc": 21,
                        "value": "[cast(fp + (-3), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 7
                        },
                        "pc": 25,
                        "value": "[cast(ap + (-2), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 17
                        },
                        "pc": 32,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.read.storage_addr": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.read.storage_addr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 7
                        },
                        "pc": 25,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.read.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.balance.read.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 0
                        },
                        "pc": 21,
                        "value": "[cast(fp + (-5), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 14
                        },
                        "pc": 29,
                        "value": "[cast(ap + (-2), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 3,
                            "offset": 15
                        },
                        "pc": 30,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.storage_read": {
                "destination": "starkware.starknet.common.syscalls.storage_read",
                "type": "alias"
            },
            "__main__.balance.storage_write": {
                "destination": "starkware.starknet.common.syscalls.storage_write",
                "type": "alias"
            },
            "__main__.balance.write": {
                "decorators": [],
                "pc": 34,
                "type": "function"
            },
            "__main__.balance.write.Args": {
                "full_name": "__main__.balance.write.Args",
                "members": {
                    "value": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.balance.write.ImplicitArgs": {
                "full_name": "__main__.balance.write.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.balance.write.Return": {
                "full_name": "__main__.balance.write.Return",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.balance.write.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.balance.write.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.balance.write.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 0
                        },
                        "pc": 34,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 7
                        },
                        "pc": 38,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.write.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.write.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 0
                        },
                        "pc": 34,
                        "value": "[cast(fp + (-4), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 7
                        },
                        "pc": 38,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.write.storage_addr": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.write.storage_addr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 7
                        },
                        "pc": 38,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.write.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.balance.write.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 0
                        },
                        "pc": 34,
                        "value": "[cast(fp + (-6), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 14
                        },
                        "pc": 43,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.balance.write.value": {
                "cairo_type": "felt",
                "full_name": "__main__.balance.write.value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 4,
                            "offset": 0
                        },
                        "pc": 34,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_balance": {
                "decorators": [
                    "view"
                ],
                "pc": 76,
                "type": "function"
            },
            "__main__.get_balance.Args": {
                "full_name": "__main__.get_balance.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.get_balance.ImplicitArgs": {
                "full_name": "__main__.get_balance.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.get_balance.Return": {
                "full_name": "__main__.get_balance.Return",
                "members": {
                    "res": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.get_balance.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.get_balance.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.get_balance.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 0
                        },
                        "pc": 76,
                        "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 23
                        },
                        "pc": 81,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_balance.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.get_balance.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 0
                        },
                        "pc": 76,
                        "value": "[cast(fp + (-3), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 23
                        },
                        "pc": 81,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_balance.res": {
                "cairo_type": "felt",
                "full_name": "__main__.get_balance.res",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 23
                        },
                        "pc": 81,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.get_balance.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.get_balance.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 0
                        },
                        "pc": 76,
                        "value": "[cast(fp + (-5), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 7,
                            "offset": 23
                        },
                        "pc": 81,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.increase_balance": {
                "decorators": [
                    "external"
                ],
                "pc": 46,
                "type": "function"
            },
            "__main__.increase_balance.Args": {
                "full_name": "__main__.increase_balance.Args",
                "members": {
                    "amount": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "__main__.increase_balance.ImplicitArgs": {
                "full_name": "__main__.increase_balance.ImplicitArgs",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__main__.increase_balance.Return": {
                "full_name": "__main__.increase_balance.Return",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__main__.increase_balance.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__main__.increase_balance.amount": {
                "cairo_type": "felt",
                "full_name": "__main__.increase_balance.amount",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 46,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.increase_balance.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__main__.increase_balance.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 46,
                        "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 23
                        },
                        "pc": 51,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 45
                        },
                        "pc": 57,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.increase_balance.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__main__.increase_balance.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 46,
                        "value": "[cast(fp + (-4), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 23
                        },
                        "pc": 51,
                        "value": "[cast(ap + (-2), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 45
                        },
                        "pc": 57,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.increase_balance.res": {
                "cairo_type": "felt",
                "full_name": "__main__.increase_balance.res",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 23
                        },
                        "pc": 51,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__main__.increase_balance.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__main__.increase_balance.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 0
                        },
                        "pc": 46,
                        "value": "[cast(fp + (-6), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 23
                        },
                        "pc": 51,
                        "value": "[cast(ap + (-4), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 5,
                            "offset": 45
                        },
                        "pc": 57,
                        "value": "[cast(ap + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance": {
                "decorators": [
                    "view"
                ],
                "pc": 91,
                "type": "function"
            },
            "__wrappers__.get_balance.Args": {
                "full_name": "__wrappers__.get_balance.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.get_balance.ImplicitArgs": {
                "full_name": "__wrappers__.get_balance.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.get_balance.Return": {
                "full_name": "__wrappers__.get_balance.Return",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "retdata": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "size": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "__wrappers__.get_balance.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.get_balance.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_balance.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 91,
                        "value": "cast([fp + (-3)] - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_balance.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 91,
                        "value": "[cast(fp + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.__wrapped_func": {
                "destination": "__main__.get_balance",
                "type": "alias"
            },
            "__wrappers__.get_balance.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.get_balance.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 91,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 28
                        },
                        "pc": 97,
                        "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_balance.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 91,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 28
                        },
                        "pc": 97,
                        "value": "[cast(ap + (-2), felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 36
                        },
                        "pc": 100,
                        "value": "[cast(ap + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.ret_struct": {
                "cairo_type": "__main__.get_balance.Return",
                "full_name": "__wrappers__.get_balance.ret_struct",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 28
                        },
                        "pc": 97,
                        "value": "[cast(ap + (-1), __main__.get_balance.Return*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_balance.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 36
                        },
                        "pc": 100,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_balance.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 36
                        },
                        "pc": 100,
                        "value": "[cast(ap + (-2), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_balance.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 0
                        },
                        "pc": 91,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 9,
                            "offset": 28
                        },
                        "pc": 97,
                        "value": "[cast(ap + (-4), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance_encode_return": {
                "decorators": [],
                "pc": 82,
                "type": "function"
            },
            "__wrappers__.get_balance_encode_return.Args": {
                "full_name": "__wrappers__.get_balance_encode_return.Args",
                "members": {
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "ret_struct": {
                        "cairo_type": "__main__.get_balance.Return",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "__wrappers__.get_balance_encode_return.ImplicitArgs": {
                "full_name": "__wrappers__.get_balance_encode_return.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.get_balance_encode_return.Return": {
                "full_name": "__wrappers__.get_balance_encode_return.Return",
                "members": {
                    "data": {
                        "cairo_type": "felt*",
                        "offset": 2
                    },
                    "data_len": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "__wrappers__.get_balance_encode_return.SIZEOF_LOCALS": {
                "type": "const",
                "value": 1
            },
            "__wrappers__.get_balance_encode_return.__return_value_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_balance_encode_return.__return_value_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 1
                        },
                        "pc": 84,
                        "value": "[cast(fp, felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 1
                        },
                        "pc": 85,
                        "value": "cast([fp] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance_encode_return.__return_value_ptr_start": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.get_balance_encode_return.__return_value_ptr_start",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 1
                        },
                        "pc": 84,
                        "value": "[cast(fp, felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance_encode_return.__temp3": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_balance_encode_return.__temp3",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 2
                        },
                        "pc": 87,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "__wrappers__.get_balance_encode_return.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.get_balance_encode_return.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 0
                        },
                        "pc": 82,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.get_balance_encode_return.ret_struct": {
                "cairo_type": "__main__.get_balance.Return",
                "full_name": "__wrappers__.get_balance_encode_return.ret_struct",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 8,
                            "offset": 0
                        },
                        "pc": 82,
                        "value": "[cast(fp + (-4), __main__.get_balance.Return*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance": {
                "decorators": [
                    "external"
                ],
                "pc": 58,
                "type": "function"
            },
            "__wrappers__.increase_balance.Args": {
                "full_name": "__wrappers__.increase_balance.Args",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.increase_balance.ImplicitArgs": {
                "full_name": "__wrappers__.increase_balance.ImplicitArgs",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "__wrappers__.increase_balance.Return": {
                "full_name": "__wrappers__.increase_balance.Return",
                "members": {
                    "pedersen_ptr": {
                        "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                        "offset": 1
                    },
                    "range_check_ptr": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "retdata": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "size": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "__wrappers__.increase_balance.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "__wrappers__.increase_balance.__calldata_actual_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.increase_balance.__calldata_actual_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.__calldata_arg_amount": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.increase_balance.__calldata_arg_amount",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "[cast([fp + (-3)], felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.__calldata_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.increase_balance.__calldata_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "[cast(fp + (-3), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "cast([fp + (-3)] + 1, felt*)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.__temp2": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.increase_balance.__temp2",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 1
                        },
                        "pc": 60,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.__wrapped_func": {
                "destination": "__main__.increase_balance",
                "type": "alias"
            },
            "__wrappers__.increase_balance.pedersen_ptr": {
                "cairo_type": "starkware.cairo.common.cairo_builtins.HashBuiltin*",
                "full_name": "__wrappers__.increase_balance.pedersen_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 52
                        },
                        "pc": 67,
                        "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.range_check_ptr": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.increase_balance.range_check_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "[cast([fp + (-5)] + 2, felt*)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 52
                        },
                        "pc": 67,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.ret_struct": {
                "cairo_type": "__main__.increase_balance.Return",
                "full_name": "__wrappers__.increase_balance.ret_struct",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 52
                        },
                        "pc": 67,
                        "value": "[cast(ap + 0, __main__.increase_balance.Return*)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.retdata": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.increase_balance.retdata",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 53
                        },
                        "pc": 69,
                        "value": "[cast(ap + (-1), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.retdata_size": {
                "cairo_type": "felt",
                "full_name": "__wrappers__.increase_balance.retdata_size",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 53
                        },
                        "pc": 69,
                        "value": "cast(0, felt)"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "__wrappers__.increase_balance.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 0
                        },
                        "pc": 58,
                        "value": "[cast([fp + (-5)], felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 6,
                            "offset": 52
                        },
                        "pc": 67,
                        "value": "[cast(ap + (-3), felt**)]"
                    }
                ],
                "type": "reference"
            },
            "__wrappers__.increase_balance_encode_return.memcpy": {
                "destination": "starkware.cairo.common.memcpy.memcpy",
                "type": "alias"
            },
            "starkware.cairo.common.cairo_builtins.BitwiseBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.BitwiseBuiltin",
                "members": {
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "x_and_y": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "x_or_y": {
                        "cairo_type": "felt",
                        "offset": 4
                    },
                    "x_xor_y": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.EcOpBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.EcOpBuiltin",
                "members": {
                    "m": {
                        "cairo_type": "felt",
                        "offset": 4
                    },
                    "p": {
                        "cairo_type": "starkware.cairo.common.ec_point.EcPoint",
                        "offset": 0
                    },
                    "q": {
                        "cairo_type": "starkware.cairo.common.ec_point.EcPoint",
                        "offset": 2
                    },
                    "r": {
                        "cairo_type": "starkware.cairo.common.ec_point.EcPoint",
                        "offset": 5
                    }
                },
                "size": 7,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.EcPoint": {
                "destination": "starkware.cairo.common.ec_point.EcPoint",
                "type": "alias"
            },
            "starkware.cairo.common.cairo_builtins.HashBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "members": {
                    "result": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.cairo_builtins.SignatureBuiltin": {
                "full_name": "starkware.cairo.common.cairo_builtins.SignatureBuiltin",
                "members": {
                    "message": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "pub_key": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.dict_access.DictAccess": {
                "full_name": "starkware.cairo.common.dict_access.DictAccess",
                "members": {
                    "key": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "new_value": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "prev_value": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.cairo.common.ec_point.EcPoint": {
                "full_name": "starkware.cairo.common.ec_point.EcPoint",
                "members": {
                    "x": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "y": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.cairo.common.hash.HashBuiltin": {
                "destination": "starkware.cairo.common.cairo_builtins.HashBuiltin",
                "type": "alias"
            },
            "starkware.starknet.common.storage.ADDR_BOUND": {
                "type": "const",
                "value": -106710729501573572985208420194530329073740042555888586719489
            },
            "starkware.starknet.common.storage.MAX_STORAGE_ITEM_SIZE": {
                "type": "const",
                "value": 256
            },
            "starkware.starknet.common.storage.assert_250_bit": {
                "destination": "starkware.cairo.common.math.assert_250_bit",
                "type": "alias"
            },
            "starkware.starknet.common.syscalls.CALL_CONTRACT_SELECTOR": {
                "type": "const",
                "value": 20853273475220472486191784820
            },
            "starkware.starknet.common.syscalls.CallContract": {
                "full_name": "starkware.starknet.common.syscalls.CallContract",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.CallContractRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.CallContractResponse",
                        "offset": 5
                    }
                },
                "size": 7,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.CallContractRequest": {
                "full_name": "starkware.starknet.common.syscalls.CallContractRequest",
                "members": {
                    "calldata": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "calldata_size": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "contract_address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "function_selector": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.CallContractResponse": {
                "full_name": "starkware.starknet.common.syscalls.CallContractResponse",
                "members": {
                    "retdata": {
                        "cairo_type": "felt*",
                        "offset": 1
                    },
                    "retdata_size": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.DELEGATE_CALL_SELECTOR": {
                "type": "const",
                "value": 21167594061783206823196716140
            },
            "starkware.starknet.common.syscalls.DELEGATE_L1_HANDLER_SELECTOR": {
                "type": "const",
                "value": 23274015802972845247556842986379118667122
            },
            "starkware.starknet.common.syscalls.DictAccess": {
                "destination": "starkware.cairo.common.dict_access.DictAccess",
                "type": "alias"
            },
            "starkware.starknet.common.syscalls.EMIT_EVENT_SELECTOR": {
                "type": "const",
                "value": 1280709301550335749748
            },
            "starkware.starknet.common.syscalls.EmitEvent": {
                "full_name": "starkware.starknet.common.syscalls.EmitEvent",
                "members": {
                    "data": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "data_len": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "keys": {
                        "cairo_type": "felt*",
                        "offset": 2
                    },
                    "keys_len": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 5,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GET_BLOCK_NUMBER_SELECTOR": {
                "type": "const",
                "value": 1448089106835523001438702345020786
            },
            "starkware.starknet.common.syscalls.GET_BLOCK_TIMESTAMP_SELECTOR": {
                "type": "const",
                "value": 24294903732626645868215235778792757751152
            },
            "starkware.starknet.common.syscalls.GET_CALLER_ADDRESS_SELECTOR": {
                "type": "const",
                "value": 94901967781393078444254803017658102643
            },
            "starkware.starknet.common.syscalls.GET_CONTRACT_ADDRESS_SELECTOR": {
                "type": "const",
                "value": 6219495360805491471215297013070624192820083
            },
            "starkware.starknet.common.syscalls.GET_SEQUENCER_ADDRESS_SELECTOR": {
                "type": "const",
                "value": 1592190833581991703053805829594610833820054387
            },
            "starkware.starknet.common.syscalls.GET_TX_INFO_SELECTOR": {
                "type": "const",
                "value": 1317029390204112103023
            },
            "starkware.starknet.common.syscalls.GET_TX_SIGNATURE_SELECTOR": {
                "type": "const",
                "value": 1448089128652340074717162277007973
            },
            "starkware.starknet.common.syscalls.GetBlockNumber": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockNumber",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockNumberRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockNumberResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockNumberRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockNumberRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockNumberResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockNumberResponse",
                "members": {
                    "block_number": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockTimestamp": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockTimestamp",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockTimestampRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetBlockTimestampResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockTimestampRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockTimestampRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetBlockTimestampResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetBlockTimestampResponse",
                "members": {
                    "block_timestamp": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetCallerAddress": {
                "full_name": "starkware.starknet.common.syscalls.GetCallerAddress",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetCallerAddressRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetCallerAddressResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetCallerAddressRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetCallerAddressRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetCallerAddressResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetCallerAddressResponse",
                "members": {
                    "caller_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetContractAddress": {
                "full_name": "starkware.starknet.common.syscalls.GetContractAddress",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetContractAddressRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetContractAddressResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetContractAddressRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetContractAddressRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetContractAddressResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetContractAddressResponse",
                "members": {
                    "contract_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetSequencerAddress": {
                "full_name": "starkware.starknet.common.syscalls.GetSequencerAddress",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetSequencerAddressRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetSequencerAddressResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetSequencerAddressRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetSequencerAddressRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetSequencerAddressResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetSequencerAddressResponse",
                "members": {
                    "sequencer_address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxInfo": {
                "full_name": "starkware.starknet.common.syscalls.GetTxInfo",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxInfoRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxInfoResponse",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxInfoRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetTxInfoRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxInfoResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetTxInfoResponse",
                "members": {
                    "tx_info": {
                        "cairo_type": "starkware.starknet.common.syscalls.TxInfo*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxSignature": {
                "full_name": "starkware.starknet.common.syscalls.GetTxSignature",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxSignatureRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.GetTxSignatureResponse",
                        "offset": 1
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxSignatureRequest": {
                "full_name": "starkware.starknet.common.syscalls.GetTxSignatureRequest",
                "members": {
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.GetTxSignatureResponse": {
                "full_name": "starkware.starknet.common.syscalls.GetTxSignatureResponse",
                "members": {
                    "signature": {
                        "cairo_type": "felt*",
                        "offset": 1
                    },
                    "signature_len": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.SEND_MESSAGE_TO_L1_SELECTOR": {
                "type": "const",
                "value": 433017908768303439907196859243777073
            },
            "starkware.starknet.common.syscalls.STORAGE_READ_SELECTOR": {
                "type": "const",
                "value": 100890693370601760042082660
            },
            "starkware.starknet.common.syscalls.STORAGE_WRITE_SELECTOR": {
                "type": "const",
                "value": 25828017502874050592466629733
            },
            "starkware.starknet.common.syscalls.SendMessageToL1SysCall": {
                "full_name": "starkware.starknet.common.syscalls.SendMessageToL1SysCall",
                "members": {
                    "payload_ptr": {
                        "cairo_type": "felt*",
                        "offset": 3
                    },
                    "payload_size": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "to_address": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 4,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageRead": {
                "full_name": "starkware.starknet.common.syscalls.StorageRead",
                "members": {
                    "request": {
                        "cairo_type": "starkware.starknet.common.syscalls.StorageReadRequest",
                        "offset": 0
                    },
                    "response": {
                        "cairo_type": "starkware.starknet.common.syscalls.StorageReadResponse",
                        "offset": 2
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageReadRequest": {
                "full_name": "starkware.starknet.common.syscalls.StorageReadRequest",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageReadResponse": {
                "full_name": "starkware.starknet.common.syscalls.StorageReadResponse",
                "members": {
                    "value": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.StorageWrite": {
                "full_name": "starkware.starknet.common.syscalls.StorageWrite",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "selector": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "value": {
                        "cairo_type": "felt",
                        "offset": 2
                    }
                },
                "size": 3,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.TxInfo": {
                "full_name": "starkware.starknet.common.syscalls.TxInfo",
                "members": {
                    "account_contract_address": {
                        "cairo_type": "felt",
                        "offset": 1
                    },
                    "chain_id": {
                        "cairo_type": "felt",
                        "offset": 6
                    },
                    "max_fee": {
                        "cairo_type": "felt",
                        "offset": 2
                    },
                    "signature": {
                        "cairo_type": "felt*",
                        "offset": 4
                    },
                    "signature_len": {
                        "cairo_type": "felt",
                        "offset": 3
                    },
                    "transaction_hash": {
                        "cairo_type": "felt",
                        "offset": 5
                    },
                    "version": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 7,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_read": {
                "decorators": [],
                "pc": 0,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.storage_read.Args": {
                "full_name": "starkware.starknet.common.syscalls.storage_read.Args",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_read.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.storage_read.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_read.Return": {
                "full_name": "starkware.starknet.common.syscalls.storage_read.Return",
                "members": {
                    "value": {
                        "cairo_type": "felt",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_read.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.storage_read.__temp0": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_read.__temp0",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 0,
                            "offset": 1
                        },
                        "pc": 2,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.address": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_read.address",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 0,
                            "offset": 0
                        },
                        "pc": 0,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.response": {
                "cairo_type": "starkware.starknet.common.syscalls.StorageReadResponse",
                "full_name": "starkware.starknet.common.syscalls.storage_read.response",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 0,
                            "offset": 1
                        },
                        "pc": 4,
                        "value": "[cast([fp + (-4)] + 2, starkware.starknet.common.syscalls.StorageReadResponse*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.syscall": {
                "cairo_type": "starkware.starknet.common.syscalls.StorageRead",
                "full_name": "starkware.starknet.common.syscalls.storage_read.syscall",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 0,
                            "offset": 0
                        },
                        "pc": 0,
                        "value": "[cast([fp + (-4)], starkware.starknet.common.syscalls.StorageRead*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_read.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.storage_read.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 0,
                            "offset": 0
                        },
                        "pc": 0,
                        "value": "[cast(fp + (-4), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 0,
                            "offset": 1
                        },
                        "pc": 4,
                        "value": "cast([fp + (-4)] + 3, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write": {
                "decorators": [],
                "pc": 8,
                "type": "function"
            },
            "starkware.starknet.common.syscalls.storage_write.Args": {
                "full_name": "starkware.starknet.common.syscalls.storage_write.Args",
                "members": {
                    "address": {
                        "cairo_type": "felt",
                        "offset": 0
                    },
                    "value": {
                        "cairo_type": "felt",
                        "offset": 1
                    }
                },
                "size": 2,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_write.ImplicitArgs": {
                "full_name": "starkware.starknet.common.syscalls.storage_write.ImplicitArgs",
                "members": {
                    "syscall_ptr": {
                        "cairo_type": "felt*",
                        "offset": 0
                    }
                },
                "size": 1,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_write.Return": {
                "full_name": "starkware.starknet.common.syscalls.storage_write.Return",
                "members": {},
                "size": 0,
                "type": "struct"
            },
            "starkware.starknet.common.syscalls.storage_write.SIZEOF_LOCALS": {
                "type": "const",
                "value": 0
            },
            "starkware.starknet.common.syscalls.storage_write.__temp1": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_write.__temp1",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 1
                        },
                        "pc": 10,
                        "value": "[cast(ap + (-1), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write.address": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_write.address",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 8,
                        "value": "[cast(fp + (-4), felt*)]"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write.syscall_ptr": {
                "cairo_type": "felt*",
                "full_name": "starkware.starknet.common.syscalls.storage_write.syscall_ptr",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 8,
                        "value": "[cast(fp + (-5), felt**)]"
                    },
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 1
                        },
                        "pc": 13,
                        "value": "cast([fp + (-5)] + 3, felt*)"
                    }
                ],
                "type": "reference"
            },
            "starkware.starknet.common.syscalls.storage_write.value": {
                "cairo_type": "felt",
                "full_name": "starkware.starknet.common.syscalls.storage_write.value",
                "references": [
                    {
                        "ap_tracking_data": {
                            "group": 1,
                            "offset": 0
                        },
                        "pc": 8,
                        "value": "[cast(fp + (-3), felt*)]"
                    }
                ],
                "type": "reference"
            }
        },
        "main_scope": "__main__",
        "prime": "0x800000000000011000000000000000000000000000000000000000000000001",
        "reference_manager": {
            "references": [
                {
                    "ap_tracking_data": {
                        "group": 0,
                        "offset": 0
                    },
                    "pc": 0,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 0,
                        "offset": 0
                    },
                    "pc": 0,
                    "value": "[cast(fp + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 0,
                        "offset": 0
                    },
                    "pc": 0,
                    "value": "[cast([fp + (-4)], starkware.starknet.common.syscalls.StorageRead*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 0,
                        "offset": 1
                    },
                    "pc": 2,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 0,
                        "offset": 1
                    },
                    "pc": 4,
                    "value": "[cast([fp + (-4)] + 2, starkware.starknet.common.syscalls.StorageReadResponse*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 0,
                        "offset": 1
                    },
                    "pc": 4,
                    "value": "cast([fp + (-4)] + 3, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 8,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 8,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 0
                    },
                    "pc": 8,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 1
                    },
                    "pc": 10,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 1,
                        "offset": 1
                    },
                    "pc": 13,
                    "value": "cast([fp + (-5)] + 3, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 0
                    },
                    "pc": 16,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 0
                    },
                    "pc": 16,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 2,
                        "offset": 0
                    },
                    "pc": 16,
                    "value": "cast(916907772491729262376534102982219947830828984996257231353398618781993312401, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 0
                    },
                    "pc": 21,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 0
                    },
                    "pc": 21,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 0
                    },
                    "pc": 21,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 7
                    },
                    "pc": 25,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 7
                    },
                    "pc": 25,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 7
                    },
                    "pc": 25,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 14
                    },
                    "pc": 29,
                    "value": "[cast(ap + (-2), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 14
                    },
                    "pc": 29,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 15
                    },
                    "pc": 30,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 16
                    },
                    "pc": 31,
                    "value": "[cast(ap + (-1), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 17
                    },
                    "pc": 32,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 3,
                        "offset": 18
                    },
                    "pc": 33,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 0
                    },
                    "pc": 34,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 0
                    },
                    "pc": 34,
                    "value": "[cast(fp + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 0
                    },
                    "pc": 34,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 0
                    },
                    "pc": 34,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 7
                    },
                    "pc": 38,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 7
                    },
                    "pc": 38,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 7
                    },
                    "pc": 38,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 4,
                        "offset": 14
                    },
                    "pc": 43,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 46,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 46,
                    "value": "[cast(fp + (-6), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 46,
                    "value": "[cast(fp + (-5), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 0
                    },
                    "pc": 46,
                    "value": "[cast(fp + (-4), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 23
                    },
                    "pc": 51,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 23
                    },
                    "pc": 51,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 23
                    },
                    "pc": 51,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 23
                    },
                    "pc": 51,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 45
                    },
                    "pc": 57,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 45
                    },
                    "pc": 57,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 5,
                        "offset": 45
                    },
                    "pc": 57,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "[cast([fp + (-3)], felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "cast([fp + (-3)] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 0
                    },
                    "pc": 58,
                    "value": "cast([fp + (-3)] + 1 - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 1
                    },
                    "pc": 60,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 52
                    },
                    "pc": 67,
                    "value": "[cast(ap + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 52
                    },
                    "pc": 67,
                    "value": "[cast(ap + (-2), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 52
                    },
                    "pc": 67,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 52
                    },
                    "pc": 67,
                    "value": "[cast(ap + 0, __main__.increase_balance.Return*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 53
                    },
                    "pc": 69,
                    "value": "[cast(ap + (-1), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 6,
                        "offset": 53
                    },
                    "pc": 69,
                    "value": "cast(0, felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 0
                    },
                    "pc": 76,
                    "value": "[cast(fp + (-5), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 0
                    },
                    "pc": 76,
                    "value": "[cast(fp + (-4), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 0
                    },
                    "pc": 76,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 23
                    },
                    "pc": 81,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 23
                    },
                    "pc": 81,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 23
                    },
                    "pc": 81,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 7,
                        "offset": 23
                    },
                    "pc": 81,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 0
                    },
                    "pc": 82,
                    "value": "[cast(fp + (-4), __main__.get_balance.Return*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 0
                    },
                    "pc": 82,
                    "value": "[cast(fp + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 1
                    },
                    "pc": 84,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 1
                    },
                    "pc": 84,
                    "value": "[cast(fp, felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 1
                    },
                    "pc": 85,
                    "value": "cast([fp] + 1, felt*)"
                },
                {
                    "ap_tracking_data": {
                        "group": 8,
                        "offset": 2
                    },
                    "pc": 87,
                    "value": "[cast(ap + (-1), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 91,
                    "value": "[cast([fp + (-5)], felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 91,
                    "value": "[cast([fp + (-5)] + 1, starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 91,
                    "value": "[cast([fp + (-5)] + 2, felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 91,
                    "value": "[cast(fp + (-3), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 0
                    },
                    "pc": 91,
                    "value": "cast([fp + (-3)] - [fp + (-3)], felt)"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 28
                    },
                    "pc": 97,
                    "value": "[cast(ap + (-4), felt**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 28
                    },
                    "pc": 97,
                    "value": "[cast(ap + (-3), starkware.cairo.common.cairo_builtins.HashBuiltin**)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 28
                    },
                    "pc": 97,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 28
                    },
                    "pc": 97,
                    "value": "[cast(ap + (-1), __main__.get_balance.Return*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 36
                    },
                    "pc": 100,
                    "value": "[cast(ap + (-3), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 36
                    },
                    "pc": 100,
                    "value": "[cast(ap + (-2), felt*)]"
                },
                {
                    "ap_tracking_data": {
                        "group": 9,
                        "offset": 36
                    },
                    "pc": 100,
                    "value": "[cast(ap + (-1), felt**)]"
                }
            ]
        }
    }
}
"""
