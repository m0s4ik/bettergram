# This file is part of Bettergram.
#
# For license and copyright information please follow this link:
# https://github.com/bettergram/bettergram/blob/master/LEGAL

{
  'conditions': [[ 'build_macstore', {
    'xcode_settings': {
      'SKIP_INSTALL': 'YES',
    }
  }]],
  'includes': [
    'common.gypi',
  ],
  'targets': [{
    'target_name': 'lib_base',
    'type': 'static_library',
    'includes': [
      'common.gypi',
	  'openssl.gypi',
      'qt.gypi',
      'telegram_win.gypi',
      'telegram_linux.gypi',
      'pch.gypi',
    ],
    'variables': {
      'src_loc': '../SourceFiles',
      'res_loc': '../Resources',
      'libs_loc': '../../../Libraries',
      'official_build_target%': '',
      'submodules_loc': '../ThirdParty',
      'pch_source': '<(src_loc)/base/base_pch.cpp',
      'pch_header': '<(src_loc)/base/base_pch.h',
    },
    'defines': [
      'XXH_INLINE_ALL',
    ],
    'dependencies': [
      'crl.gyp:crl',
    ],
    'include_dirs': [
      '<(src_loc)',
      '<(SHARED_INTERMEDIATE_DIR)',
      '<(libs_loc)/range-v3/include',
      '<(submodules_loc)/GSL/include',
      '<(submodules_loc)/variant/include',
      '<(submodules_loc)/crl/src',
      '<(submodules_loc)/xxHash',
    ],
    'sources': [
      '<(src_loc)/base/algorithm.h',
      '<(src_loc)/base/assertion.h',
      '<(src_loc)/base/basic_types.h',
      '<(src_loc)/base/binary_guard.h',
      '<(src_loc)/base/build_config.h',
      '<(src_loc)/base/bytes.h',
      '<(src_loc)/base/concurrent_timer.cpp',
      '<(src_loc)/base/concurrent_timer.h',
      '<(src_loc)/base/flags.h',
      '<(src_loc)/base/enum_mask.h',
      '<(src_loc)/base/flat_map.h',
      '<(src_loc)/base/flat_set.h',
      '<(src_loc)/base/functors.h',
      '<(src_loc)/base/index_based_iterator.h',
	  '<(src_loc)/base/last_used_cache.h',
      '<(src_loc)/base/match_method.h',
      '<(src_loc)/base/observer.cpp',
      '<(src_loc)/base/observer.h',
      '<(src_loc)/base/ordered_set.h',
      '<(src_loc)/base/openssl_help.h',
      '<(src_loc)/base/optional.h',
      '<(src_loc)/base/overload.h',
      '<(src_loc)/base/parse_helper.cpp',
      '<(src_loc)/base/parse_helper.h',
      '<(src_loc)/base/qthelp_regex.h',
      '<(src_loc)/base/qthelp_url.cpp',
      '<(src_loc)/base/qthelp_url.h',
      '<(src_loc)/base/runtime_composer.cpp',
      '<(src_loc)/base/runtime_composer.h',
      '<(src_loc)/base/timer.cpp',
      '<(src_loc)/base/timer.h',
      '<(src_loc)/base/type_traits.h',
      '<(src_loc)/base/unique_any.h',
      '<(src_loc)/base/unique_function.h',
      '<(src_loc)/base/unique_qptr.h',
      '<(src_loc)/base/value_ordering.h',
      '<(src_loc)/base/variant.h',
      '<(src_loc)/base/virtual_method.h',
      '<(src_loc)/base/weak_ptr.h',
      '<(src_loc)/base/zlib_help.h',
    ],
    'conditions': [[ 'build_macold', {
      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [ '-nostdinc++' ],
      },
      'include_dirs': [
        '/usr/local/macold/include/c++/v1',
      ],
    }]],
  }],
}
