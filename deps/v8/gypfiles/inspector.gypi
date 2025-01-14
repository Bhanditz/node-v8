# Copyright 2016 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'protocol_path': '../third_party/inspector_protocol',
    'inspector_path': '../src/inspector',

    'inspector_generated_sources': [
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Forward.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Protocol.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Protocol.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Console.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Console.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Debugger.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Debugger.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/HeapProfiler.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/HeapProfiler.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Profiler.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Profiler.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Runtime.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Runtime.h',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Schema.cpp',
      '<(SHARED_INTERMEDIATE_DIR)/src/inspector/protocol/Schema.h',
      '<(SHARED_INTERMEDIATE_DIR)/include/inspector/Debugger.h',
      '<(SHARED_INTERMEDIATE_DIR)/include/inspector/Runtime.h',
      '<(SHARED_INTERMEDIATE_DIR)/include/inspector/Schema.h',
    ],

    'inspector_all_sources': [
      '../include/v8-inspector.h',
      '../include/v8-inspector-protocol.h',
      '../src/inspector/custom-preview.cc',
      '../src/inspector/custom-preview.h',
      '../src/inspector/injected-script.cc',
      '../src/inspector/injected-script.h',
      '../src/inspector/inspected-context.cc',
      '../src/inspector/inspected-context.h',
      '../src/inspector/remote-object-id.cc',
      '../src/inspector/remote-object-id.h',
      '../src/inspector/search-util.cc',
      '../src/inspector/search-util.h',
      '../src/inspector/string-16.cc',
      '../src/inspector/string-16.h',
      '../src/inspector/string-util.cc',
      '../src/inspector/string-util.h',
      '../src/inspector/test-interface.cc',
      '../src/inspector/test-interface.h',
      '../src/inspector/v8-console.cc',
      '../src/inspector/v8-console.h',
      '../src/inspector/v8-console-agent-impl.cc',
      '../src/inspector/v8-console-agent-impl.h',
      '../src/inspector/v8-console-message.cc',
      '../src/inspector/v8-console-message.h',
      '../src/inspector/v8-debugger.cc',
      '../src/inspector/v8-debugger.h',
      '../src/inspector/v8-debugger-agent-impl.cc',
      '../src/inspector/v8-debugger-agent-impl.h',
      '../src/inspector/v8-debugger-script.cc',
      '../src/inspector/v8-debugger-script.h',
      '../src/inspector/v8-heap-profiler-agent-impl.cc',
      '../src/inspector/v8-heap-profiler-agent-impl.h',
      '../src/inspector/v8-inspector-impl.cc',
      '../src/inspector/v8-inspector-impl.h',
      '../src/inspector/v8-inspector-session-impl.cc',
      '../src/inspector/v8-inspector-session-impl.h',
      '../src/inspector/v8-profiler-agent-impl.cc',
      '../src/inspector/v8-profiler-agent-impl.h',
      '../src/inspector/v8-regex.cc',
      '../src/inspector/v8-regex.h',
      '../src/inspector/v8-runtime-agent-impl.cc',
      '../src/inspector/v8-runtime-agent-impl.h',
      '../src/inspector/v8-schema-agent-impl.cc',
      '../src/inspector/v8-schema-agent-impl.h',
      '../src/inspector/v8-stack-trace-impl.cc',
      '../src/inspector/v8-stack-trace-impl.h',
      '../src/inspector/v8-value-utils.cc',
      '../src/inspector/v8-value-utils.h',
      '../src/inspector/value-mirror.cc',
      '../src/inspector/value-mirror.h',
      '../src/inspector/wasm-translation.cc',
      '../src/inspector/wasm-translation.h',
    ]
  },
  'includes': [
    '../third_party/inspector_protocol/inspector_protocol.gypi',
  ],
  'actions': [
    {
      'action_name': 'protocol_compatibility',
      'inputs': [
        '<(inspector_path)/js_protocol.json',
      ],
      'outputs': [
        '<@(SHARED_INTERMEDIATE_DIR)/src/js_protocol.stamp',
      ],
      'action': [
        'python',
        '<(protocol_path)/check_protocol_compatibility.py',
        '--stamp', '<@(_outputs)',
        '<(inspector_path)/js_protocol.json',
      ],
      'message': 'Checking inspector protocol compatibility',
    },
    {
      'action_name': 'protocol_generated_sources',
      'inputs': [
        '<(inspector_path)/js_protocol.json',
        '<(inspector_path)/inspector_protocol_config.json',
        '<@(inspector_protocol_files)',
      ],
      'outputs': [
        '<@(inspector_generated_sources)',
      ],
      'process_outputs_as_sources': 1,
      'action': [
        'python',
        '<(protocol_path)/code_generator.py',
        '--jinja_dir', '../third_party',
        '--output_base', '<(SHARED_INTERMEDIATE_DIR)/src/inspector',
        '--config', '<(inspector_path)/inspector_protocol_config.json',
      ],
      'message': 'Generating inspector protocol sources from protocol json',
    },
  ],
}
